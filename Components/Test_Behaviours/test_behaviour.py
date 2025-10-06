import pygame as py
from pygame import Vector2

from Classes import Behaviour
from Systems import InputSystem
from Components import *

class TestBehaviour(Behaviour):
    def update(self):
        keys = InputSystem.get_keys()
        if keys[py.K_d]:
            self.owner.get_component(Rigidbody).set_velocity(Vector2(0, 200))
