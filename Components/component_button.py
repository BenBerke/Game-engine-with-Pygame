import pygame as py
from config import SCREEN

from Classes import Component
from Classes.class_GUI_element import GUIElement

class Button(Component, GUIElement):
    def __init__(self, screen=SCREEN, x=200, y=20, width=500, height=50, is_editor=None):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_editor = is_editor
        Component.__init__(self)
        GUIElement.__init__(self, x=self.x, y=self.y, width=self.width, height=self.height, is_editor=self.is_editor, anchor_point="middle_center")

    def render(self, screen):
        py.draw.rect(screen, (255, 0, 0), py.Rect(self.x, self.y, self.width, self.height))

    def to_dict(self):
        return {
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "is_editor": self.is_editor,
            "appear_in_debug": self.appear_in_debugger,
            # Optionally save other relevant fields
        }
