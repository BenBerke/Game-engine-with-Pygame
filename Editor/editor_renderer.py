import pygame as py
from config import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH_CENTER, SCREEN_HEIGHT_CENTER, PIXELS_PER_UNIT
import config
from Components import Transform

class EditorRenderer:

    @classmethod
    def render_scene(cls, camera, sprites, texts, guis):
        SCREEN.fill((230, 230, 230))
        cls.draw_grid(camera)

        for renderer in sorted(sprites, key=lambda r: r.render_order):
            if renderer.is_world_pos:
                transform = renderer.owner.get_component(Transform)
                screen_pos = camera.world_to_screen(transform.position)
                screen_scale = transform.scale * camera.zoom * PIXELS_PER_UNIT
                renderer.render(screen=SCREEN, position=screen_pos, scale=screen_scale)
            else:
                renderer.render(screen=SCREEN)

        # Render world text
        for text in sorted(texts, key=lambda r: r.render_order):
            if text.is_world_pos:
                owner_transform = text.owner.get_component(Transform)
                if owner_transform:
                    screen_pos = camera.world_to_screen(owner_transform.world_position)
                    text.position = screen_pos
            text.render(screen=SCREEN)

        for gui in sorted(guis, key=lambda r: r.render_order):
            if gui:
                gui.render(screen=SCREEN)

        # Add more editor overlays (selection box, handles, etc.)

        py.display.flip()

    @classmethod
    def draw_grid(cls, camera):
        if not config.EDITOR_MODE: return

        grid_color = (200, 200, 200)
        spacing = PIXELS_PER_UNIT * camera.zoom
        start_x = -camera.position.x * camera.zoom + SCREEN_WIDTH_CENTER
        start_y = camera.position.y * camera.zoom + SCREEN_HEIGHT_CENTER

        # Draw vertical lines
        x = start_x % spacing
        while x < SCREEN_WIDTH:
            current_color = (0, 0, 0) if x == start_x else grid_color
            py.draw.line(SCREEN, current_color, (x, 0), (x, SCREEN_HEIGHT))
            x += spacing

        # Draw horizontal lines
        y = start_y % spacing
        while y < SCREEN_HEIGHT:
            current_color = (0, 0, 0) if y == start_y else grid_color
            py.draw.line(SCREEN, current_color, (0, y), (SCREEN_WIDTH, y))
            y += spacing
