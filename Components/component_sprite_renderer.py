import pygame as py
from pygame import Vector2

from config import INIT_DISPLAY as SCREEN, PIXELS_PER_UNIT
from Systems import RenderingSystem
from Components import Transform
from Classes import Component, Sprite

class SpriteRenderer(Component):
    def __init__(self, sprite=None, color=(0,0,0), render_order=0, is_world_pos=True, scale=Vector2(1,1)):
        super().__init__()
        self.owner = None
        self.color = color
        self.render_order = render_order
        self.is_world_pos = is_world_pos
        self.scale = scale

        if isinstance(sprite, Sprite):
            self.sprite = sprite
            sprite_data = sprite.to_dict()
        elif isinstance(sprite, dict):
            self.sprite = Sprite(
                sprite_path=sprite.get("sprite_path"),
                width=sprite.get("width", 5),
                height=sprite.get("height", 5)
            )
            sprite_data = sprite
        else:
            self.sprite = None
            sprite_data = None

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
        # Use provided position & scale from RenderingSystem
        pos = position if position else self.owner.get_component(Transform).screen_position
        scale = scale if scale else self.owner.get_component(Transform).scale

        # Prepare image
        if self.sprite and hasattr(self.sprite, "image"):
            image = py.transform.scale(self.sprite.image, (int(scale.x + self.scale.x * PIXELS_PER_UNIT), int(scale.y + self.scale.y * PIXELS_PER_UNIT)))
        else:
            # Fallback: colored rectangle
            image = py.Surface((int(scale.x + self.scale.x * PIXELS_PER_UNIT), int(scale.y + self.scale.y * PIXELS_PER_UNIT)), py.SRCALPHA)
            image.fill(self.color)

        # Center the image at pos
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
