import pygame as py
from pygame import Vector2

class InputSystem:
    _keys_down = set()
    _keys_up = set()
    _keys = None
    _mouse_down = set()
    _mouse_up = set()
    _mouse_buttons = None
    _events = []

    @classmethod
    def update(cls, events):
        cls._events = events
        cls._keys = py.key.get_pressed()
        cls._keys_down.clear()
        cls._keys_up.clear()
        cls._mouse_down.clear()
        cls._mouse_up.clear()

        for event in events:
            if event.type == py.KEYDOWN:
                cls._keys_down.add(event.key)
            elif event.type == py.KEYUP:
                cls._keys_up.add(event.key)
            elif event.type == py.MOUSEBUTTONDOWN:
                cls._mouse_down.add(event.button)
            elif event.type == py.MOUSEBUTTONUP:
                cls._mouse_up.add(event.button)

    # -------- Keyboard --------
    @classmethod
    def is_key_pressed(cls, key):
        """Is the key currently held down?"""
        return cls._keys[key]

    @classmethod
    def was_key_pressed(cls, key):
        """Was the key pressed this frame?"""
        return key in cls._keys_down

    @classmethod
    def was_key_released(cls, key):
        """Was the key released this frame?"""
        return key in cls._keys_up

    # -------- Mouse --------
    @classmethod
    def get_mouse_pos(cls):
        return cls._mouse_pos

    @classmethod
    def is_mouse_pressed(cls, button=1):
        """Is the mouse button held down? 1=Left, 2=Middle, 3=Right"""
        return cls._mouse_buttons[button-1] if cls._mouse_buttons else False

    @classmethod
    def was_mouse_pressed(cls, button=1):
        """Was the mouse button pressed this frame?"""
        return button in cls._mouse_down

    @classmethod
    def was_mouse_released(cls, button=1):
        """Was the mouse button released this frame?"""
        return button in cls._mouse_up

    @classmethod
    def get_events(cls):
        """Return raw pygame events."""
        return cls._events

    @classmethod
    def refresh_mouse_state(cls):
        """Call after update() to refresh current mouse buttons state."""
        cls._mouse_buttons = py.mouse.get_pressed()
