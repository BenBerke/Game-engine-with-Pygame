import pygame as py

class InputSystem:
    keys = []
    events = []

    @classmethod
    def update(cls):
        # Poll events once per frame
        cls.events = py.event.get()
        cls.keys = py.key.get_pressed()
        cls.keys = py.key.get_pressed()

    @classmethod
    def get_events(cls):
        return cls.events

    @classmethod
    def get_keys(cls):
        return cls.keys
