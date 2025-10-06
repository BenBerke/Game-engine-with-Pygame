import pygame as py
from pygame import Vector2
import config

from config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER
from Components import SpriteRenderer, Rigidbody, Transform, BoxCollider
from Components import TestBehaviour
from Classes import Scene, Object, Sprite, DebugConsole
from Systems import PhysicsSystem, RenderingSystem, InputSystem, system_time_manager

from Systems import system_scene_loader

py.init()
SCREEN = config.INIT_DISPLAY()
clock = py.time.Clock()
running = True


myobj = Object.create(
    name="myobject",
    components=[Rigidbody(debug_mode=False), TestBehaviour(), SpriteRenderer(), BoxCollider()],
)

floor = Object.create(
    name="floor",
    components=[Transform(world_position=Vector2(0, -200), scale=Vector2(500, 10)), SpriteRenderer(), BoxCollider()],
)

#Scene.save_scene("Rb_test")

debug_console = DebugConsole(max_lines=15)

frame=0

while running:
    frame += 1
    InputSystem.update()

    for event in InputSystem.get_events():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                running = False

    system_time_manager.dt = clock.tick(60) / 1000

    PhysicsSystem.update()
    Scene.update()
    RenderingSystem.update()

    obj_velocity = myobj.get_component(Rigidbody).velocity
    debug_console.log(f"FPS:{int(clock.get_fps())}", line=0)
    debug_console.render(SCREEN)

