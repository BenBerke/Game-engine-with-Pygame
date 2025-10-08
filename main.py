import pygame as py
import config

from Classes import Scene
from Systems import PhysicsSystem, RenderingSystem, InputSystem, system_time_manager
from Editor.editor_system import EditorSystem
from Engine.engine_script_loader import load_custom_behaviours
from Systems.system_scene_loader import load_scene

py.init()
SCREEN = config.INIT_DISPLAY()
clock = py.time.Clock()
running = True
CUSTOM_BEHAVIOURS = load_custom_behaviours("Assets")

load_scene("Assets/Test_Scenes/save_test.json", custom_behaviours=CUSTOM_BEHAVIOURS)

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
