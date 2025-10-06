class Object:
    id_counter = 0

    def __init__(self, name, components):
        self.id = Object.id_counter
        Object.id_counter += 1
        self.name = name
        self.components = {}

    @classmethod
    def create(cls, name="GameObject", components=()):
        obj = cls(name, components)

        from Components import Transform
        transform = next((c for c in components if isinstance(c, Transform)), None)
        if transform is None:
            transform = Transform()
        obj.add_component(transform)

        for comp in components:
            if isinstance(comp, Transform):
                continue
            obj.add_component(comp)

        from Classes import Scene
        Scene.register_object(obj)

        for comp in obj.components.values():
            if hasattr(comp, "start"):
                comp.start()

        return obj

    def add_component(self, component):
        component_type = type(component).__name__
        self.components[component_type] = component
        component.owner = self

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
        from Components import SpriteRenderer, BoxCollider, Rigidbody
        for comp in self.components.values():
            if isinstance(comp, (SpriteRenderer, BoxCollider, Rigidbody)):
                continue
            if hasattr(comp, "update"):
                comp.update()

    def remove(self):
        from Classes import Scene
        Scene.remove_object(self)
