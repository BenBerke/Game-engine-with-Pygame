import pygame as py
import config

from config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER
from Components import Rigidbody, TestBehaviour, Transform
from Classes import Scene, Object
from Systems import PhysicsSystem, RenderingSystem, InputSystem, system_time_manager

from Systems import system_scene_loader

py.init()
SCREEN = config.INIT_DISPLAY()
clock = py.time.Clock()
running = True


system_scene_loader.load_scene("Test_Scenes/kemal.json")

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

