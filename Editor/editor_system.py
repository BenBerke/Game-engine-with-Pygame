import pygame as py

from Components import SpriteRenderer, Transform
from Editor.editor_camera import EditorCamera
from Editor.editor_renderer import EditorRenderer
from Systems import RenderingSystem, Scene
import config
from Systems.system_scene_loader import load_scene


class EditorSystem:
    active_scene = None

    def __init__(self):
        self.camera = EditorCamera()

    def update(self):
        EditorRenderer.render_scene(
            camera=self.camera,
            sprites=RenderingSystem.sprites,
            texts=RenderingSystem.text
        )

        for obj in Scene.objects:
            if obj.get_component(SpriteRenderer):
                transform = obj.get_component(Transform)
                print(transform.screen_position, transform.scale)

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
