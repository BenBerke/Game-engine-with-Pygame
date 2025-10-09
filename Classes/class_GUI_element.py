from config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER
from Systems import RenderingSystem

class GUIElement():
    anchor_points = {"top_left": (0, 0), "top_center": (SCREEN_WIDTH_CENTER, 0), "top_right": (SCREEN_WIDTH, 0),
                     "middle_left": (0, SCREEN_HEIGHT_CENTER), "middle_center": (SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER), "middle_right": (SCREEN_WIDTH, SCREEN_HEIGHT_CENTER),
                     "bottom_left": (0, SCREEN_HEIGHT), "bottom_center": (SCREEN_WIDTH_CENTER, SCREEN_HEIGHT), "bottom_right": (SCREEN_WIDTH, SCREEN_HEIGHT)}

    def __init__(self, x=50, y=50, width=50, height=50, anchor_point=None, render_order=0, is_editor=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_editor = is_editor
        self.render_order = render_order
        self.anchor_point = self.anchor_points[anchor_point]
        if is_editor:
            RenderingSystem.register_editor_gui(self)
        else:
            RenderingSystem.register_gui(self)

    def get_screen_position(self):
        anchor_x, anchor_y = self.anchor_point
        return anchor_x + self.x, anchor_y + self.y

    def render(self, screen):
        pass

    def update(self):
        pass

    def on_remove(self):
        if self.is_editor:
            RenderingSystem.unregister_editor_gui(self)
        else:
            RenderingSystem.unregister_gui(self)