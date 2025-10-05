import pygame as py

class Sprite:
    def __init__(self, sprite_path=None, width=500, height=500):
        self.width = width
        self.height = height
        self.owner = None

        if sprite_path:
            self.file_name = sprite_path
            self.sprite_path = f"Sprites/{sprite_path}.png"
            self.image = py.image.load(self.sprite_path).convert_alpha()
            self.image = py.transform.scale(self.image, (width, height))
        else:
            self.image = py.Surface((width, height), py.SRCALPHA)

    def to_dict(self):
        return {
            "sprite_path": self.file_name,
            "width": self.width,
            "height": self.height
        }