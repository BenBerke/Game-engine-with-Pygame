from pygame import Vector2
from config import PIXELS_PER_UNIT, SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER
from Classes import Component, Scene
from Components import Transform

class Camera(Component):
    def __init__(self, viewport_dimensions=Vector2(50, 50), zoom=1):
        self.viewport_dimensions = viewport_dimensions
        self.zoom = zoom

        if Scene.main_camera is None:
            Scene.main_camera = self

    def world_to_screen(self, world_position):
        cam_transform = self.owner.get_component(Transform)
        offset = world_position - cam_transform.position
        offset *= self.zoom
        offset_pixels = Vector2(offset) * PIXELS_PER_UNIT
        offset.y *= -1
        screen_pos = Vector2(SCREEN_WIDTH_CENTER + offset_pixels.x, SCREEN_HEIGHT_CENTER - offset_pixels.y)
        return screen_pos