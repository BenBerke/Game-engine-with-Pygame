import pygame as py
from pygame import Vector2
from config import INIT_DISPLAY
import config
SCREEN = INIT_DISPLAY()

from Systems.system_physics import PhysicsSystem
from Components.component_transform import Transform
from Classes.class_component import Component


class BoxCollider(Component):
    def __init__(self, width=None, height=None, offset=Vector2(0,0), draw_gizmo=False):
        super().__init__()
        self.width = width
        self.draw_gizmo = draw_gizmo
        self.height = height
        self.offset = offset
        PhysicsSystem.register_collider(self)

    def start(self):
        if self.owner is None:
            return
        transform = self.owner.get_component(Transform)
        if not self.width:
            self.width = transform.scale.x
        if not self.height:
            self.height = transform.scale.y

    def update(self):
        pass


    def on_remove(self):
        PhysicsSystem.unregister_collider(self)

    def rect(self):
        transform = self.owner.get_component(Transform)
        pos = transform.position + self.offset
        w = self.width
        h = self.height
        x = pos.x - w / 2
        y = pos.y - h / 2
        return(x, y, w, h)

