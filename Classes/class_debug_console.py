import pygame as py
from Systems import RenderingSystem

class DebugConsole:
    def __init__(self, max_lines=10, font=None, color=(0,0,0), position=(0,0), size=24):
        self.max_lines = max_lines
        self.lines = [""] * max_lines  # pre-fill with empty strings

        if font is not None:
            self.font = font
        else:
            self.font = py.font.Font(None, size)
        self.color = color
        self.position = position

        RenderingSystem.register_debug_console(self)


    def log(self, text, line=-1):
        """
        Log a line.
        If line >= 0, overwrite that line.
        If line < 0, append to the console as usual.
        """
        if line >= 0 and line < self.max_lines:
            self.lines[line] = str(text)
        else:
            self.lines.append(str(text))
            if len(self.lines) > self.max_lines:
                self.lines.pop(0)

    def render(self, screen):
        x, y = self.position
        for line in self.lines:
            text_surface = self.font.render(line, True, self.color)
            screen.blit(text_surface, (x, y))
            y += self.font.get_height()
