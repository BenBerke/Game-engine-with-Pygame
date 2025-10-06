import pygame as py
from config import INIT_DISPLAY, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER
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
        SCREEN.fill((255, 255, 255))
        py.draw.line(SCREEN, (0, 0, 0), (SCREEN_WIDTH_CENTER, 0), (SCREEN_WIDTH_CENTER, SCREEN_HEIGHT))
        py.draw.line(SCREEN, (0, 0, 0), (0, SCREEN_HEIGHT_CENTER), (SCREEN_WIDTH, SCREEN_HEIGHT_CENTER))

        for renderer in sorted(cls.sprites, key=lambda r: r.render_order):
            renderer.render(SCREEN)
        for text in sorted(cls.text, key=lambda r: r.render_order):
            text.render(SCREEN)

        if cls.debug_console:
            cls.debug_console.render(SCREEN)

        py.display.flip()