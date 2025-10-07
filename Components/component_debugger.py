from pygame import Vector2
from config import SCREEN
from Classes import Component, Object
from Components import TextRenderer, Transform
from Classes import Scene

class Debugger(Component):
    ignore_in_save = True
    def __init__(self, screen=SCREEN, size=18):
        super().__init__()
        self.screen = screen
        self.size = size
        self.owner = None
        self.debug_text_object = None
        self.text_renderer = None
        self.appear_in_debug = False

    def start(self):
        # Create a runtime-only TextRenderer object for debug display
        self.debug_text_object = Object.create(
            name=f"{self.owner.name}_debug_text",
            components=[TextRenderer(text="", size=self.size, color=(0, 0, 0), is_world_pos=False)]
        )
        # Mark it so scene saving can ignore it
        self.debug_text_object.ignore_in_save = True
        self.text_renderer = self.debug_text_object.get_component(TextRenderer)

    def update(self):
        if not self.text_renderer:
            return

        engine_debug = ""
        behaviour_debug = ""

        engine_debug += f"ID: {self.owner.id}\n"
        engine_debug += f"Name: {self.owner.name}\n"

        # Build the debug string
        for comp_name, comp in self.owner.components.items():
            if not getattr(comp, "appear_in_debug", True):
                continue

            block = f"{comp_name}\n"
            for attr_name, value in vars(comp).items():
                if attr_name in ("owner", "appear_in_debug"):
                    continue
                block += f"    {attr_name}: {value}\n"

            # Behaviours go at the bottom
            from Classes import CustomBehaviour
            if issubclass(type(comp), CustomBehaviour):
                behaviour_debug += block
            else:
                engine_debug += block

        debug_string = engine_debug
        if behaviour_debug:
            debug_string += "\n--CUSTOM BEHAVIOURS--\n" + behaviour_debug

        # Update the TextRenderer
        self.text_renderer.text = debug_string

        # Get the object's transform
        owner_transform = self.owner.get_component(Transform)
        if owner_transform:
            # Convert world position to screen position using the main camera
            if hasattr(Scene, "main_camera") and Scene.main_camera:
                screen_pos = Scene.main_camera.world_to_screen(owner_transform.world_position)
            else:
                # fallback: just use world_position relative to screen center
                screen_pos = Vector2(
                    SCREEN.get_width() // 2 + owner_transform.world_position.x,
                    SCREEN.get_height() // 2 - owner_transform.world_position.y
                )

            # Offset the text to appear above and to the right of the object
            offset = Vector2(owner_transform.scale.x * 40, owner_transform.scale.y * -20)
            self.text_renderer.position = screen_pos + offset
