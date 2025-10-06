import pygame as py
from pygame import Vector2

from Classes import CustomBehaviour, DebugConsole, Scene
from Systems import InputSystem
from Components import *

class TestBehaviour(CustomBehaviour):
    def __init__(self):
        super().__init__()
        self.move_speed = 30
        self.jump_power = 500

    def update(self):
        transform = self.owner.get_component(Transform)
        if InputSystem.is_key_pressed(py.K_a):
            transform.translate(Vector2(-self.move_speed, 0))
        if InputSystem.is_key_pressed(py.K_d):
            transform.translate(Vector2(self.move_speed, 0))
        if InputSystem.is_key_pressed(py.K_w):
            transform.translate(Vector2(0, self.move_speed))
        if InputSystem.is_key_pressed(py.K_s):
            transform.translate(Vector2(0, -self.move_speed))

        # Example: do something on D release
        if InputSystem.was_key_released(py.K_d):
            pass

