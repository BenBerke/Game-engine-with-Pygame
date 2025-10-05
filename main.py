import pygame as py

import config
from Components import Rigidbody
from Systems import system_time_manager

from Classes.class_object import Object
from Components.Test_Behaviours.test_behaviour import TestBehaviour
from config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER

from Classes.class_scene_manager import Scene

from Systems.system_input import InputSystem
from Systems.system_rendering import RenderingSystem
from Systems.system_physics import PhysicsSystem

py.init()
SCREEN = config.INIT_DISPLAY()
clock = py.time.Clock()
running = True

myobj = Object(
    name="my name",
    components=[TestBehaviour(), Rigidbody()],
)

while running:
    InputSystem.update()
    for event in InputSystem.get_events():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                running = False

    SCREEN.fill((255, 255, 255))
    py.draw.line(SCREEN, (0, 0, 0), (SCREEN_WIDTH_CENTER, 0), (SCREEN_WIDTH_CENTER, SCREEN_HEIGHT))
    py.draw.line(SCREEN, (0, 0, 0), (0, SCREEN_HEIGHT_CENTER), (SCREEN_WIDTH, SCREEN_HEIGHT_CENTER))

    system_time_manager.dt = clock.tick(60) / 1000


    PhysicsSystem.update()
    RenderingSystem.update()
    Scene.update()


    py.display.flip()

