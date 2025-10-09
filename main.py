import pygame as py
import config
from pygame import Vector2
from Assets.Test_Behaviours.test_behaviour import TestBehaviour

from Classes import Scene, Object, DebugConsole
from Systems import PhysicsSystem, RenderingSystem, InputSystem, system_time_manager
from Components import SpriteRenderer, Debugger, Camera, BoxCollider, Rigidbody, Transform, Button
from Editor.editor_system import EditorSystem
from Engine.engine_script_loader import load_custom_behaviours
from Systems.system_scene_loader import load_scene

py.init()
SCREEN = config.INIT_DISPLAY()
clock = py.time.Clock()
running = True
CUSTOM_BEHAVIOURS = load_custom_behaviours("Assets")

# cam = Object.create(
#     name="camera",
#     components=[Camera()]
# )
#
# my_obj = Object.create(
#     name="my_obj",
#     components=[SpriteRenderer(), TestBehaviour(), BoxCollider(), Rigidbody(), Button(is_editor=False)],
# )
#
# floor = Object.create(
#     name="floor",
#     components=[SpriteRenderer(), BoxCollider(), Transform(position=Vector2(0, -150), scale=Vector2(10, .1))],
# )

load_scene("Test_Scenes/gui_test")

debug_console = DebugConsole(max_lines=15)

while running:
    events = py.event.get()
    InputSystem.update(events)

    for event in InputSystem.get_events():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            #pause
            if event.key == py.K_F1:
                if not config.EDITOR_MODE:
                    config.PAUSED = not config.PAUSED
            #stop
            if event.key == py.K_F2:
                if config.EDITOR_MODE:
                    EditorSystem.switch_to_game_mode()
                else:
                    EditorSystem.switch_to_editor_mode()

    system_time_manager.dt = clock.tick(60) / 1000
    debug_console.log(f"FPS:{int(clock.get_fps())}", line=0)

    editor_system = EditorSystem() if config.EDITOR_MODE else None

    if config.EDITOR_MODE or config.PAUSED:
        editor_system = EditorSystem()
        editor_system.update()

    else:
        RenderingSystem.update()
        PhysicsSystem.update()
        Scene.update()



py.quit()