from Classes import Component
from Components import *

class Behaviour(Component):
    def __init__(self):
        super().__init__()
        self.owner = None

    def start(self):
        pass
    def update(self):
        pass
    def on_remove(self):
        pass