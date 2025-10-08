import pygame as py
from pygame import Vector2

from config import SCREEN, PIXELS_PER_UNIT
from Systems import RenderingSystem
from Components import Transform
from Classes import Component, Sprite

class SpriteRenderer(Component):
    def __init__(self, sprite=None, color=(0,0,0), render_order=0, is_world_pos=True):
        super().__init__()
        self.owner = None
        self.color = color
        self.render_order = render_order
        self.is_world_pos = is_world_pos

        if isinstance(sprite, Sprite):
            self.sprite = sprite
        elif isinstance(sprite, dict):
            self.sprite = Sprite(
                sprite_path=sprite.get("sprite_path"),
                width=sprite.get("width", 5),
                height=sprite.get("height", 5)
            )
        else:
            self.sprite = None

        RenderingSystem.register_sprite(self)

    def to_dict(self):
        data = super().to_dict()  # Include normal attributes
        if self.sprite:
            # Store only serializable info, not the Surface
            data["sprite"] = {
                "sprite_path": getattr(self.sprite, "sprite_path", None),
                "width": getattr(self.sprite, "width", None),
                "height": getattr(self.sprite, "height", None)
            }
        else:
            data["sprite"] = None

        return data

    def render(self, screen=SCREEN, position=None, scale=None):
        from Classes import Scene
        from config import SCREEN  # get actual surface
        if screen is None:
            screen = SCREEN

        transform = self.owner.get_component(Transform)

        # Get position in pixels
        if self.is_world_pos and Scene.main_camera:
            pos = Scene.main_camera.world_to_screen(transform.position)
            zoom = Scene.main_camera.zoom
        else:
            pos = transform.position
            zoom = 1

        # Determine size in pixels
        if self.sprite and hasattr(self.sprite, "width") and hasattr(self.sprite, "height"):
            # Base sprite size in pixels
            base_width = self.sprite.width
            base_height = self.sprite.height
            px_width = int(base_width * transform.scale.x * zoom)
            px_height = int(base_height * transform.scale.y * zoom)
        else:
            # Fallback square in world units converted to pixels
            px_width = int(transform.scale.x * PIXELS_PER_UNIT * zoom)
            px_height = int(transform.scale.y * PIXELS_PER_UNIT * zoom)

        # Prepare image
        if self.sprite and hasattr(self.sprite, "image"):
            image = py.transform.scale(self.sprite.image, (px_width, px_height))
        else:
            image = py.Surface((px_width, px_height), py.SRCALPHA)
            image.fill(self.color)

        rect = image.get_rect(center=(int(pos.x), int(pos.y)))
        screen.blit(image, rect)

    def change_sprite(self, sprite=None):
        if isinstance(sprite, dict):
            self.sprite = Sprite(
                sprite_path=sprite.get("sprite_path"),
                width=sprite.get("width", 500),
                height=sprite.get("height", 500)
            )
        else:
            self.sprite = sprite

    def on_remove(self):
        RenderingSystem.unregister_sprite(self)
