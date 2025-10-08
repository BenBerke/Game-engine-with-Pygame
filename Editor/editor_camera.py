import pygame as py
from pygame import Vector2
from config import SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER, PIXELS_PER_UNIT

class EditorCamera:
    def __init__(self):
        self.position = Vector2(0, 0)
        self.zoom = 1.0
        self.pan_speed = 500  # pixels per second
        self.zoom_speed = 0.1

    def world_to_screen(self, world_pos: Vector2) -> Vector2:
        """Convert world coordinates to screen coordinates."""
        offset = world_pos - self.position
        offset *= self.zoom
        offset_pixels = Vector2(offset) * PIXELS_PER_UNIT
        offset.y *= -1
        screen_pos = Vector2(SCREEN_WIDTH_CENTER + offset_pixels.x, SCREEN_HEIGHT_CENTER - offset_pixels.y)
        return screen_pos

    def screen_to_world(self, screen_pos: Vector2) -> Vector2:
        """Convert screen coordinates to world coordinates."""
        return (screen_pos - Vector2(SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER)) / self.zoom + self.position

    def update(self, dt):
        """Move the camera based on keyboard input."""
        keys = py.key.get_pressed()

        # Pan camera
        if keys[py.K_LEFT]:
            self.position.x -= self.pan_speed * dt / self.zoom
        if keys[py.K_RIGHT]:
            self.position.x += self.pan_speed * dt / self.zoom
        if keys[py.K_UP]:
            self.position.y += self.pan_speed * dt / self.zoom
        if keys[py.K_DOWN]:
            self.position.y -= self.pan_speed * dt / self.zoom

    def handle_event(self, event):
        """Handle mouse wheel zooming."""
        if event.type == py.MOUSEWHEEL:
            if event.y > 0:
                self.zoom += self.zoom_speed
            elif event.y < 0:
                self.zoom = max(0.1, self.zoom - self.zoom_speed)
