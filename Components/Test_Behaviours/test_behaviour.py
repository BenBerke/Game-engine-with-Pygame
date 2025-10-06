import pygame as py
from pygame import Vector2

from Classes import CustomBehaviour, DebugConsole, Scene
from Systems import InputSystem
from Components import *

class TestBehaviour(CustomBehaviour):
    def __init__(self):
        super().__init__()
        self.move_speed = 30
        self.jump_power = 100

    def update(self):
        transform = self.owner.get_component(Transform)
        camera_transform = Scene.main_camera.owner.get_component(Transform)
        if InputSystem.is_key_pressed(py.K_a):
            transform.translate(Vector2(-self.move_speed, 0))
        if InputSystem.is_key_pressed(py.K_d):
            transform.translate(Vector2(self.move_speed, 0))
        if InputSystem.is_key_pressed(py.K_w):
            self.owner.get_component(Rigidbody).add_force(Vector2(0, self.jump_power))
        if InputSystem.is_key_pressed(py.K_s):
            transform.translate(Vector2(0, -self.move_speed))

        if InputSystem.is_key_pressed(py.K_r):
            Scene.main_camera.zoom += .5
        if InputSystem.is_key_pressed(py.K_q):
            Scene.main_camera.zoom -= .5

        if InputSystem.is_key_pressed(py.K_RIGHT):
            camera_transform.translate(Vector2(self.move_speed, 0))
        if InputSystem.is_key_pressed(py.K_LEFT):
            camera_transform.translate(Vector2(-self.move_speed, 0))
        if InputSystem.is_key_pressed(py.K_UP):
            camera_transform.translate(Vector2(0, self.move_speed))
        if InputSystem.is_key_pressed(py.K_DOWN):
            camera_transform.translate(Vector2(0, -self.move_speed))

        # Example: do something on D release
        if InputSystem.was_key_released(py.K_d):
            pass

