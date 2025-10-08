import pygame as py
import config
from config import INIT_DISPLAY, SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER, PIXELS_PER_UNIT
from Classes import Scene


SCREEN = INIT_DISPLAY()

class RenderingSystem:
    sprites = []
    text = []
    debug_console = None

    @classmethod
    def register_debug_console(cls, console):
        cls.debug_console = console

    @classmethod
    def register_sprite(cls, sprite):
        cls.sprites.append(sprite)

    @classmethod
    def unregister_sprite(cls, sprite):
        if sprite in cls.sprites:
            cls.sprites.remove(sprite)

    @classmethod
    def register_text(cls, text):
        cls.text.append(text)

    @classmethod
    def unregister_text(cls, text):
        if text in cls.text:
            cls.text.remove(text)

    @classmethod
    def update(cls):
        cam = Scene.main_camera
        if config.EDITOR_MODE:
            return
        if cam is None:
            py.font.init()
            font = py.font.Font(None, 64)
            SCREEN.fill((0,0,0))
            text_surface = font.render("NO CAMERA DETECTED", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER))
            SCREEN.blit(text_surface, text_rect)

            py.display.flip()
            return

        SCREEN.fill((255, 255, 255))

        # Render sprites
        from Components import Transform
        for renderer in sorted(cls.sprites, key=lambda r: r.render_order):
            if renderer.is_world_pos:
                transform = renderer.owner.get_component(Transform)
                screen_pos = cam.world_to_screen(transform.position)
                screen_scale = transform.scale * cam.zoom * PIXELS_PER_UNIT
                renderer.render(screen=SCREEN, position=screen_pos, scale=screen_scale)
            else:
                renderer.render(screen=SCREEN)

        # Render world text
        for text in sorted(cls.text, key=lambda r: r.render_order):
            if text.is_world_pos:
                owner_transform = text.owner.get_component(Transform)
                if owner_transform:
                    screen_pos = cam.world_to_screen(owner_transform.world_position)
                    # Update text position each frame
                    text.position = screen_pos
            text.render(screen=SCREEN)

        # Render debug console (if exists)
        if cls.debug_console:
            cls.debug_console.render(SCREEN)

        py.display.flip()
