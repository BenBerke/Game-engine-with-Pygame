from pygame import Vector2
from config import SCREEN
from Classes import Component, Object, CustomBehaviour
from Components import TextRenderer, Transform

class Debugger(Component):
    def __init__(self, screen=SCREEN, size=18):
        super().__init__()
        self.screen = screen
        self.size = size
        self.owner = None
        self.debug_text_object = None
        self.text_renderer = None
        self.appear_in_debug = False

    def start(self):
        # Create the TextRenderer object
        self.debug_text_object = Object.create(
            name=f"{self.owner.name}_debug_text",
            components=[TextRenderer(text="", size=self.size, color=(0,0,0))]
        )
        self.text_renderer = self.debug_text_object.get_component(TextRenderer)

    def update(self):
        if not self.text_renderer:
            return

        engine_debug = ""
        behaviour_debug = ""

        # Separate normal components from custom behaviours
        for comp_name, comp in self.owner.components.items():
            if not getattr(comp, "appear_in_debug", True):
                continue

            block = f"{comp_name}\n"
            for attr_name, value in vars(comp).items():
                if attr_name in ("owner", "appear_in_debug"):
                    continue
                block += f"    {attr_name}: {value}\n"
            if issubclass(type(comp), CustomBehaviour):
                behaviour_debug += block
            else:
                engine_debug += block

        debug_string = engine_debug
        if behaviour_debug:
            debug_string += "\n--CUSTOM BEHAVIOURS--\n"
            debug_string += behaviour_debug

        # Update the text
        self.text_renderer.text = debug_string

        # Make the text follow the owner (top-right corner)
        owner_transform = self.owner.get_component(Transform)
        if owner_transform:
            top_right = Vector2(
                owner_transform.screen_position.x,
                owner_transform.screen_position.y
            )
            # Small offset so it doesn’t overlap the object
            self.text_renderer.position = top_right + Vector2(owner_transform.scale.x/2, -owner_transform.scale.y*2)
