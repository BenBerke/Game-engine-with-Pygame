import pygame as py
from pygame import Vector2
from config import INIT_DISPLAY
import config
SCREEN = INIT_DISPLAY()

from Systems.system_physics import PhysicsSystem
from Components.component_transform import Transform
from Classes.class_component import Component


class BoxCollider(Component):
    def __init__(self, width=0, height=0, offset=Vector2(0,0)):
        super().__init__()
        self.width = width
        self.height = height
        self.offset = offset
        PhysicsSystem.register_collider(self)

    def on_remove(self):
        PhysicsSystem.unregister_collider(self)

    def rect(self):
        transform = self.owner.get_component(Transform)
        pos = transform.position + self.offset
        w = self.width + transform.scale.x
        h = self.height + transform.scale.y
        x = pos.x - w / 2
        y = pos.y - h / 2
        return(x, y, w, h)

