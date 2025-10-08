from Editor.editor_camera import EditorCamera
from Editor.editor_renderer import EditorRenderer
from Systems import RenderingSystem
import config

class EditorSystem:
    def __init__(self):
        self.camera = EditorCamera()

    def update(self):
        EditorRenderer.render_scene(
            camera=self.camera,
            sprites=RenderingSystem.sprites,
            texts=RenderingSystem.text
        )

    def switch_to_editor_mode(self):
        if config.EDITOR_MODE:
            return
        config.EDITOR_MODE = True

    def switch_to_game_mode(self):
        if not config.EDITOR_MODE:
            return
        config.EDITOR_MODE = False
