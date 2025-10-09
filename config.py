import pygame as py
from pygame import Vector2

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 900
SCREEN_WIDTH_CENTER = SCREEN_WIDTH / 2
SCREEN_HEIGHT_CENTER = SCREEN_HEIGHT / 2

DEFUALT_GRAVITY = 8
DEFAULT_MAX_VELOCITY_X = 60
DEFAULT_MAX_VELOCITY_Y = 60
DEFAULT_FRICTION = Vector2(.09, 0)
VELOCITY_THRESHOLD = 0.1

PIXELS_PER_UNIT = 50

EDITOR_MODE = True
PAUSED = False

SCENE_SURFACE = None # Offscreen surface for game/world rendering
GUI_SURFACE = None   # Offscreen surface for GUI/editor overlays

def INIT_DISPLAY():
    global SCREEN, SCENE_SURFACE, GUI_SURFACE
    if SCREEN is None:
        # Create main window
        SCREEN = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Create offscreen surfaces
        SCENE_SURFACE = py.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        GUI_SURFACE = py.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), py.SRCALPHA)  # transparent for GUI

    return SCREEN