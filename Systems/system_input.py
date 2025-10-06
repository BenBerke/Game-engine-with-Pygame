import pygame as py

class InputSystem:
    _keys = None
    _events = []
    _keys_down = set()  # keys pressed this frame
    _keys_up = set()    # keys released this frame

    @classmethod
    def update(cls):
        """Call once per frame at the start of your loop."""
        cls._events = py.event.get()
        cls._keys = py.key.get_pressed()
        cls._keys_down.clear()
        cls._keys_up.clear()

        for event in cls._events:
            if event.type == py.KEYDOWN:
                cls._keys_down.add(event.key)
            elif event.type == py.KEYUP:
                cls._keys_up.add(event.key)

    @classmethod
    def get_keys(cls):
        """Return all currently held keys (like GetKey)."""
        return cls._keys

    @classmethod
    def get_keydown(cls):
        """Return keys pressed this frame (like GetKeyDown)."""
        return cls._keys_down

    @classmethod
    def get_keyup(cls):
        """Return keys released this frame (like GetKeyUp)."""
        return cls._keys_up

    @classmethod
    def get_events(cls):
        """Return all currently held keys (like GetKey)."""
        return cls._events

    @classmethod
    def is_key_pressed(cls, key):
        """Check if a key is currently held."""
        return cls._keys[key]

    @classmethod
    def was_key_pressed(cls, key):
        """Check if a key was pressed this frame."""
        return key in cls._keys_down

    @classmethod
    def was_key_released(cls, key):
        """Check if a key was released this frame."""
        return key in cls._keys_up
