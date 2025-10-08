import pygame as py

from Components import SpriteRenderer, Transform
from Editor.editor_camera import EditorCamera
from Editor.editor_renderer import EditorRenderer
from Systems import RenderingSystem, Scene, InputSystem
import config
from config import PIXELS_PER_UNIT
from Systems.system_scene_loader import load_scene

class EditorSystem:
    active_scene = None

    def __init__(self):
        self.camera = EditorCamera()

    """Function gets called if the mouse hovers over an object with sprite renderer in editor mode"""
    def on_hover(self, obj):
        pass

    def on_click(self, obj):
        print(obj.name)

    def update(self):
        EditorRenderer.render_scene(
            camera=self.camera,
            sprites=RenderingSystem.sprites,
            texts=RenderingSystem.text
        )

        # for obj in Scene.objects:
        #     if obj.get_component(SpriteRenderer):
        #         transform = obj.get_component(Transform)
        #         screen_pos = transform.screen_position
        #         mouse_pos = InputSystem.get_mouse_pos()
        #         width = transform.scale.x * PIXELS_PER_UNIT
        #         heigth = transform.scale.y * PIXELS_PER_UNIT
        #         left_x = screen_pos.x - (width / 2)
        #         right_x = screen_pos.x + (width / 2)
        #         top_y = screen_pos.y - (heigth / 2)
        #         bottom_y = screen_pos.y + (heigth / 2)
        #         if mouse_pos[0] > left_x and mouse_pos[0] < right_x and mouse_pos[1] > top_y and mouse_pos[1] < bottom_y:
        #             if InputSystem.was_mouse_pressed(1):
        #                 self.on_click(obj)

    @classmethod
    def switch_to_editor_mode(cls):
        if config.EDITOR_MODE:
            return
        Scene.reset_scene()
        config.EDITOR_MODE = True

    @classmethod
    def switch_to_game_mode(cls):
        if not config.EDITOR_MODE:
            return
        config.EDITOR_MODE = False

    @classmethod
    def reset_scene(cls):
        Scene.reset_scene()
        load_scene(Scene.active_scene_file)
