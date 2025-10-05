import json
from pygame.math import Vector2
from Classes import Object
from Classes import Scene
from Components import Transform, BoxCollider, SpriteRenderer, Rigidbody

# Map component names in JSON to classes
component_map = {
    "Transform": Transform,
    "BoxCollider": BoxCollider,
    "SpriteRenderer": SpriteRenderer,
    "Rigidbody": Rigidbody
}

def load_scene(file_name):
    filename = f"Scenes/{file_name}.json"
    with open(filename, "r") as f:
        data = json.load(f)

    for obj_id, obj_data in data.items():
        name = obj_data.get("name", "GameObject")
        components = []

        # Recreate components
        for comp_name, comp_attrs in obj_data["components"].items():
            comp_cls = component_map[comp_name]
            # Convert lists of length 2 to Vector2 if needed
            for key, val in comp_attrs.items():
                if isinstance(val, list) and len(val) == 2 and all(isinstance(n, (int,float)) for n in val):
                    comp_attrs[key] = Vector2(*val)

            component_instance = comp_cls(**comp_attrs)
            components.append(component_instance)

        # Create the object with its components (Transform included)
        obj = Object(name=name, components=components)
        Scene.register_object(obj)
