import pygame as py
from pygame import Vector2

from config import INIT_DISPLAY as SCREEN
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
            sprite_data = sprite.to_dict()
        elif isinstance(sprite, dict):
            self.sprite = Sprite(
                sprite_path=sprite.get("sprite_path"),
                width=sprite.get("width", 500),
                height=sprite.get("height", 500)
            )
            sprite_data = sprite
        else:
            self.sprite = None
            sprite_data = None

        RenderingSystem.register_sprite(self)

    def to_dict(self):
        data = super().to_dict()  # get all normal attributes
        if self.sprite:
            # Convert Sprite instance to a dictionary for JSON
            if hasattr(self.sprite, "to_dict"):
                data["sprite"] = self.sprite.to_dict()
            else:
                data["sprite"] = None
        return data

    def render(self, screen=SCREEN, position=Vector2(0,0), scale=1):
        self.screen = screen
        owner_transform = self.owner.get_component(Transform)
        scale = owner_transform.scale
        rot = owner_transform.rotation

        if self.sprite and hasattr(self.sprite, "image"):
            image = py.transform.scale(self.sprite.image, (scale.x * scale, scale.y * scale))
            image = py.transform.rotate(image, -rot)
        else:
            image = py.Surface((scale.x, scale.y), py.SRCALPHA)
            image.fill(self.color)

        rect = image.get_rect(center=position)
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
