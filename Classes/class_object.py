from Classes import Scene

class Object:
    id_counter = 0

    def __init__(self, name="GameObject", components=()):
        self.id = Object.id_counter
        Object.id_counter += 1
        self.name = name
        self.components = {}

        # Add any extra components
        for comp in components:
            self.add_component(comp)

        Scene.register_object(self)

    def add_component(self, component):
        component_type = type(component).__name__
        self.components[component_type] = component
        component.owner = self
        if hasattr(component, "start"):
            component.start()

    def get_component(self, component_type):
        return self.components.get(component_type.__name__, None)

    def remove_component(self, component_type):
        key = component_type.__name__
        if key in self.components:
            component = self.components[key]
            if hasattr(component, "on_remove"):
                component.on_remove()
            del self.components[key]

    def update(self):
        for comp in self.components.values():
            if isinstance(comp, (SpriteRenderer, BoxCollider, Rigidbody)):
                continue
            if hasattr(comp, "update"):
                comp.update()

    def remove(self):
        Scene.remove_object(self)
