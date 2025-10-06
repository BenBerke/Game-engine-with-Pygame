import pygame as py
from pygame import Vector2

from Components.component_text_renderer import TextRenderer
from config import DEFUALT_GRAVITY, DEFAULT_MAX_VELOCITY_X, DEFAULT_MAX_VELOCITY_Y, DEFAULT_FRICTION
from Classes import Component, Object
from Systems import PhysicsSystem

import Systems.system_time_manager

class Rigidbody(Component):
    velocity = Vector2(0,0)

    def __init__(self, gravity_scale=DEFUALT_GRAVITY, max_velocity_x = DEFAULT_MAX_VELOCITY_X, max_velocity_y = DEFAULT_MAX_VELOCITY_Y, friction=DEFAULT_FRICTION, is_kinematic=False, debug_mode=False):
        super().__init__()
        self.gravity_scale = gravity_scale
        self.max_velocity_x = max_velocity_x
        self.max_velocity_y = max_velocity_y
        self.friction = friction
        self.is_kinematic = is_kinematic
        self.debug_mode = debug_mode
        self.owner = None

        if self.debug_mode:
            self.debug_text = Object.create(
                name="debug_text",
                components=[TextRenderer()],
            )

    def start(self):
        PhysicsSystem.register_rigidbody(self)

    def update(self):
        from Components import Transform
        owner_transform = self.owner.get_component(Transform)
        if self.is_kinematic:
            return
        self.velocity.y += self.gravity_scale * Systems.system_time_manager.dt
        self.velocity.x *= (1 - self.friction.x)
        self.velocity.x = max(min(self.velocity.x, self.max_velocity_x), -self.max_velocity_x)
        owner_transform.world_position += Vector2(self.velocity.x, -self.velocity.y) * Systems.system_time_manager.dt

        if self.debug_mode:
            text = (f"Name: {self.owner.name} \n"
                    f"Velocity: {int(self.velocity.y)}")
            self.debug_text.get_component(TextRenderer).text = text


    def on_remove(self):
        PhysicsSystem.unregister_rigidbody(self)

    def add_force(self, direction:Vector2):
        self.velocity.x += direction.x
        self.velocity.y -= direction.y

    def set_velocity(self, vel):
        self.velocity = vel