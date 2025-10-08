import pygame as py
import config

from pygame import Vector2

from Classes import Scene, Object
from Components import Debugger, Camera, SpriteRenderer, Transform, Rigidbody, BoxCollider
from Components.Test_Behaviours.test_behaviour import TestBehaviour
from Systems import PhysicsSystem, RenderingSystem, InputSystem, system_time_manager
from Editor.editor_system import EditorSystem
from Systems.system_scene_loader import load_scene

py.init()
SCREEN = config.INIT_DISPLAY()
clock = py.time.Clock()
running = True

load_scene("Test_Scenes/save_test.json")

while running:
    InputSystem.update()

    for event in InputSystem.get_events():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN and event.key == py.K_F1:
            config.EDITOR_MODE = not config.EDITOR_MODE


    system_time_manager.dt = clock.tick(60) / 1000

    editor_system = EditorSystem() if config.EDITOR_MODE else None

    if config.EDITOR_MODE:
        editor_system = EditorSystem()
        editor_system.update()
    else:
        PhysicsSystem.update()
        Scene.update()
        RenderingSystem.update()
