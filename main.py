import pygame as py
import config

from Classes import Scene
from Systems import PhysicsSystem, RenderingSystem, InputSystem, system_time_manager
from config import EDITOR_MODE

py.init()
SCREEN = config.INIT_DISPLAY()
clock = py.time.Clock()
running = True

while running:
    InputSystem.update()

    for event in InputSystem.get_events():
        if event.type == py.QUIT:
            running = False
    system_time_manager.dt = clock.tick(60) / 1000

    if EDITOR_MODE:
        continue

    PhysicsSystem.update()
    Scene.update()
    RenderingSystem.update()
