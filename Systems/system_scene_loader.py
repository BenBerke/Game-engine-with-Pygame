import json
from pygame.math import Vector2
from Classes import Object, Scene
from inspect import signature

def load_scene(file_name):
    from Components import Transform, BoxCollider, SpriteRenderer, Rigidbody, TextRenderer, Debugger
    from Classes import CustomBehaviour

    component_map = {
        "Transform": Transform,
        "BoxCollider": BoxCollider,
        "SpriteRenderer": SpriteRenderer,
        "Rigidbody": Rigidbody,
        "TextRenderer": TextRenderer,
        "CustomBehaviour": CustomBehaviour,
        "Debugger": Debugger
    }

    filename = f"Scenes/{file_name}.json"
    with open(filename, "r") as f:
        data = json.load(f)

    for obj_id, obj_data in data.items():
        name = obj_data.get("name", "GameObject")
        components = []

        for comp_name, comp_attrs in obj_data["components"].items():
            # Get component class
            comp_cls = component_map.get(comp_name)
            if not comp_cls:
                print(f"[Warning] Unknown component: {comp_name}")
                continue

            # Filter kwargs to only those accepted by __init__
            init_params = signature(comp_cls.__init__).parameters
            init_kwargs = {}
            for k, v in comp_attrs.items():
                if k in init_params:
                    # Convert 2-element lists to Vector2
                    if isinstance(v, list) and len(v) == 2 and all(isinstance(n, (int, float)) for n in v):
                        v = Vector2(*v)
                    init_kwargs[k] = v

            # Create component instance
            comp_instance = comp_cls(**init_kwargs)

            # Set extra attributes that are not constructor args
            for k, v in comp_attrs.items():
                if k not in init_kwargs:
                    # Convert 2-element lists to Vector2 if needed
                    if isinstance(v, list) and len(v) == 2 and all(isinstance(n, (int, float)) for n in v):
                        v = Vector2(*v)
                    setattr(comp_instance, k, v)

            components.append(comp_instance)

        # Ensure Transform exists
        if not any(isinstance(c, Transform) for c in components):
            components.append(Transform())

        # Create object and register it
        obj = Object.create(name=name, components=components)
        Scene.register_object(obj)
