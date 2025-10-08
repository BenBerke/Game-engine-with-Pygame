from pygame.math import Vector2
from Classes import Component
from config import SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER, PIXELS_PER_UNIT


class Transform(Component):
    def __init__(self, position=None, scale=None, rotation=0):
        super().__init__()
        self.owner = None
        self.position = Vector2(position.x, position.y) if position else Vector2(0, 0)
        self.scale = Vector2(scale) if scale else Vector2(1, 1)
        self.rotation = rotation
        self.screen_position = Vector2(
            SCREEN_WIDTH_CENTER + self.position.x * PIXELS_PER_UNIT,
            SCREEN_HEIGHT_CENTER - self.position.y * PIXELS_PER_UNIT
        )

    def update(self):
        self.screen_position = Vector2(SCREEN_WIDTH_CENTER + self.position.x * PIXELS_PER_UNIT, SCREEN_HEIGHT_CENTER - self.position.y * PIXELS_PER_UNIT)

    def to_dict(self):
        return {
            "position": [int(self.position.x), int(self.position.y)],
            "scale": [int(self.scale.x), int(self.scale.y)],
            "rotation": int(self.rotation)
        }

    def set_pos(self, pos):
        self.position = Vector2(SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER) + Vector2(pos.x, pos.y)

    def set_rot(self, x):
        self.rotation = x

    def set_scale(self, scale):
        self.scale = scale

    def add_rot(self, r=0):
        self.set_rot(self.rotation + r)

    def translate(self, offset):
        self.position += Vector2(offset)
