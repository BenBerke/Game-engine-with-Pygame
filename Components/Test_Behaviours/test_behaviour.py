import pygame as py
from Classes import Behaviour
from Systems import InputSystem

class TestBehaviour(Behaviour):
    def update(self):
        keys = InputSystem.get_keys()
        if keys[py.K_d]:
            self.owner.get_component(Rigidbody)
