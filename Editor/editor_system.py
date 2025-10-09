from Components import SpriteRenderer, Transform
from Systems import RenderingSystem, Scene, InputSystem
import config
from config import PIXELS_PER_UNIT
from Systems.system_scene_loader import load_scene

class EditorSystem:
    active_scene = None

    def __init__(self):
        from Editor import EditorCamera
        self.camera = EditorCamera()

    """Function gets called if the mouse hovers over an object with sprite renderer in editor mode"""
    def on_hover(self, obj):
        pass

    def on_click(self, obj):
        pass


    def update(self):
        from Editor import EditorRenderer
        EditorRenderer.render_scene(
            camera=self.camera,
            sprites=RenderingSystem.sprites,
            texts=RenderingSystem.texts,
        )

        from Editor import EditorGUIManager
        for obj in Scene.objects:
            if obj.get_component(SpriteRenderer):
                transform = obj.get_component(Transform)
                screen_pos = transform.screen_position
                width = transform.scale.x * PIXELS_PER_UNIT
                height = transform.scale.y * PIXELS_PER_UNIT
                left_x, right_x, top_y, bottom_y = EditorGUIManager.get_screen_measurements(x=screen_pos.x,y=screen_pos.y, width=width,height=height)
                if EditorGUIManager.is_mouse_inside(left_x=left_x, right_x=right_x, top_y=top_y, bottom_y=bottom_y):
                    if InputSystem.was_mouse_pressed(1):
                        self.on_click(obj)
                        break

    @classmethod
    def switch_to_editor_mode(cls):
        if config.EDITOR_MODE:
            return
        config.EDITOR_MODE = True
        Scene.reset_scene()

    @classmethod
    def switch_to_game_mode(cls):
        if not config.EDITOR_MODE:
            return
        config.EDITOR_MODE = False
        Scene.reset_scene()

    @classmethod
    def reset_scene(cls):
        Scene.reset_scene()
        load_scene(Scene.active_scene_file)
