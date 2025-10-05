from pygame import Vector2

class Component:
    def __init__(self):
        self.owner = None  # skip this in serialization

    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            if key == "owner":
                continue  # skip circular reference
            if isinstance(value, Vector2):
                result[key] = [value.x, value.y]
            elif isinstance(value, Component):
                # nested component, serialize recursively
                result[key] = value.to_dict()
            elif hasattr(value, "to_dict"):
                result[key] = value.to_dict()
            else:
                result[key] = value
        return result

    def start(self):
        pass

    def update(self):
        pass
    def on_remove(self):
        pass

