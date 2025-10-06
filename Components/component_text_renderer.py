import pygame as py
from pygame import Vector2
from Classes import Component
from config import INIT_DISPLAY as SCREEN
from Systems import RenderingSystem

class TextRenderer(Component):
    def __init__(self, text="text", font=None, size=50, color=(0,0,0), position=Vector2(0, 0), render_order=0, is_world_pos = False, anti_aliasing=True):
        Component.__init__(self)
        self.text = text
        self.font = font
        self.size = size
        self.color = color
        self.position = position
        self.render_order = render_order
        self.is_world_pos = is_world_pos
        self.anti_aliasing = anti_aliasing

        self.font = font if font else py.font.Font(None, self.size)

        RenderingSystem.register_text(self)

    def render(self, screen=SCREEN, position=None):
        # Use provided position if given, otherwise fallback
        pos = position if position is not None else self.position

        lines = self.text.split("\n")
        for i, line in enumerate(lines):
            text_surface = self.font.render(line, self.anti_aliasing, self.color)
            screen.blit(
                text_surface,
                (pos.x, pos.y + i * (self.font.get_height() + 2))
            )

    def on_remove(self):
        RenderingSystem.unregister_text(self)

