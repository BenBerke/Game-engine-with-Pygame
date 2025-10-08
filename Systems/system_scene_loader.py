import json
from pygame.math import Vector2
from Classes import Object, Scene
from inspect import signature
from Engine.engine_script_loader import load_custom_behaviours

def load_scene(filename, base_path="Assets"):
    from Classes import CustomBehaviour
    from Components import Transform, BoxCollider, SpriteRenderer, Rigidbody, TextRenderer, Debugger, Camera

    # Load all user-defined custom behaviours automatically
    CUSTOM_BEHAVIOURS = load_custom_behaviours(base_path)

    component_map = {
        "Transform": Transform,
        "BoxCollider": BoxCollider,
        "SpriteRenderer": SpriteRenderer,
        "Rigidbody": Rigidbody,
        "TextRenderer": TextRenderer,
        "CustomBehaviour": CustomBehaviour,
        "Debugger": Debugger,
        "Camera": Camera,
    }

    # Ensure file path
    if not filename.endswith(".json"):
        filename += ".json"
    full_path = f"{base_path}/{filename}"

    with open(full_path, "r") as f:
        data = json.load(f)

    Scene.active_scene_file = filename

    loaded_objects = []

    for obj_id, obj_data in data.items():
        name = obj_data.get("name", "GameObject")
        components = []

        for comp_name, comp_attrs in obj_data["components"].items():
            # Try standard components or user-defined custom behaviours
            comp_cls = component_map.get(comp_name) or CUSTOM_BEHAVIOURS.get(comp_name)
            if not comp_cls:
                print(f"[Warning] Unknown component: {comp_name}")
                continue

            # Prepare constructor kwargs
            init_params = signature(comp_cls.__init__).parameters
            init_kwargs = {}
            for k, v in comp_attrs.items():
                if k in init_params:
                    # Convert 2-element lists to Vector2
                    if isinstance(v, list) and len(v) == 2 and all(isinstance(n, (int, float)) for n in v):
                        v = Vector2(*v)
                    init_kwargs[k] = v

            comp_instance = comp_cls(**init_kwargs)

            # Set extra attributes not in constructor
            for k, v in comp_attrs.items():
                if k not in init_kwargs:
                    if isinstance(v, list) and len(v) == 2 and all(isinstance(n, (int, float)) for n in v):
                        v = Vector2(*v)
                    setattr(comp_instance, k, v)

            components.append(comp_instance)

        # Ensure every object has a Transform
        if not any(isinstance(c, Transform) for c in components):
            components.append(Transform())

        # Create and register the object
        obj = Object.create(name=name, components=components)
        Scene.register_object(obj)
        loaded_objects.append(obj)

    # Assign first camera found in scene
    for obj in loaded_objects:
        camera = obj.get_component(Camera)
        if camera:
            Scene.main_camera = camera
            break

    if Scene.main_camera is None:
        print("[Warning] No camera found in scene!")
