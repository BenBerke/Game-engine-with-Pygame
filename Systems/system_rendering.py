from config import INIT_DISPLAY
SCREEN = INIT_DISPLAY()

class RenderingSystem:
    sprites = []

    @classmethod
    def register(cls, sprite):
        cls.sprites.append(sprite)

    @classmethod
    def unregister(cls, sprite):
        if sprite in cls.sprites:
            cls.sprites.remove(sprite)

    @classmethod
    def update(cls):
        for renderer in sorted(cls.sprites, key=lambda r: r.render_order):
            renderer.render(SCREEN)