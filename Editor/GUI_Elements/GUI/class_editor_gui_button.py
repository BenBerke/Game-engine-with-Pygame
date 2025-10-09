import pygame as py
from Classes import GUIElement
from Systems import InputSystem

class EditorGUIButton(GUIElement):
    def __init__(self, x=0, y=0, width=50, height=50, anchor_point=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.anchor_point = anchor_point
        GUIElement.__init__(self, x=self.x, y=self.y, width=self.width, height=self.height, anchor_point=self.anchor_point, is_editor=True)

    def on_click(self):
        print("clicked")

    def update(self):
        pass

    def render(self, screen):
        py.draw.rect(screen, (255, 0, 0), py.Rect(self.anchor_point[0] + self.x - self.width/2, self.anchor_point[1] - self.y - self.height/2, self.width, self.height))