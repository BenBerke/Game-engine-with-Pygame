from pygame.math import Vector2
from Classes import Component
from config import SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER

class Transform(Component):
    def __init__(self, world_position=None, scale=None, rotation=0):
        super().__init__()
        self.owner = None
        self.world_position = Vector2(world_position.x, world_position.y) if world_position else Vector2(0, 0)
        self.scale = Vector2(scale) if scale else Vector2(100, 100)
        self.rotation = rotation
        self.screen_position = Vector2(
            SCREEN_WIDTH_CENTER + self.world_position.x,
            SCREEN_HEIGHT_CENTER - self.world_position.y
        )

    def update(self):
        self.screen_position = Vector2(SCREEN_WIDTH_CENTER + self.world_position.x, SCREEN_HEIGHT_CENTER - self.world_position.y)

    def to_dict(self):
        return {
            "world_position": [int(self.world_position.x), int(self.world_position.y)],
            "scale": [int(self.scale.x), int(self.scale.y)],
            "rotation": int(self.rotation)
        }

    def set_pos(self, pos):
        self.world_position = Vector2(SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER) + Vector2(pos.x, pos.y)

    def set_rot(self, x):
        self.rotation = x

    def set_scale(self, scale):
        self.scale = scale

    def add_rot(self, r=0):
        self.set_rot(self.rotation + r)

    def translate(self, offset):
        self.world_position += Vector2(offset)
