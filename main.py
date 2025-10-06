import pygame as py
from pygame import Vector2
import config

from config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER
from Components import SpriteRenderer, Rigidbody, Transform, BoxCollider, Debugger, TextRenderer, Camera
from Components import TestBehaviour
from Classes import Scene, Object, Sprite, DebugConsole
from Systems import PhysicsSystem, RenderingSystem, InputSystem, system_time_manager, system_scene_loader

py.init()
SCREEN = config.INIT_DISPLAY()
clock = py.time.Clock()
running = True


my_camera = Object.create(
    name="my_camera",
    components=[Camera(), Transform()],
)

my_obj = Object.create(
    name="my_obj",
    components=[SpriteRenderer(), BoxCollider(), Debugger(), TestBehaviour()],
)

floor = Object.create(
    name="floor",
    components=[SpriteRenderer(), BoxCollider(), Transform(world_position=Vector2(0, -300), scale=Vector2(300, 10)), Debugger()],
)

test_text = Object.create(
    name="test_text",
    components=[(TextRenderer(position=Vector2(0, 1500), is_world_pos=True)), Transform(world_position=Vector2(150, 150))]
)

debug_console = DebugConsole(max_lines=15)

frame=0

while running:
    frame += 1
    InputSystem.update()

    for event in InputSystem.get_events():
        if event.type == py.QUIT:
            running = False
    if InputSystem.was_key_pressed(py.K_ESCAPE):
        running = False

    system_time_manager.dt = clock.tick(60) / 1000

    PhysicsSystem.update()
    Scene.update()
    RenderingSystem.update()

    debug_console.log(f"FPS:{int(clock.get_fps())}", line=0)
    debug_console.render(SCREEN)

