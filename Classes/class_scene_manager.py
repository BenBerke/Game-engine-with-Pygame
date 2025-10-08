import json

class Scene:
    objects = []
    active_scene_file = None

    main_camera = None

    @classmethod
    def register_object(cls, obj):
        cls.objects.append(obj)

    @classmethod
    def remove_object(cls, obj):
        if obj in cls.objects:
            cls.objects.remove(obj)

    @classmethod
    def save_scene(cls, filename, base_path="Assets"):
        scene_dict = {}
        for obj in cls.objects:
            if getattr(obj, "ignore_in_save", False):
                continue
            obj_dict = {
                "name": obj.name,
                "components": {}
            }
            for comp_name, comp in obj.components.items():
                if getattr(comp, "ignore_in_save", False):
                    continue
                if hasattr(comp, "to_dict"):
                    obj_dict["components"][comp_name] = comp.to_dict()
            scene_dict[obj.id] = obj_dict

        if not filename.endswith(".json"):
            filename += ".json"
        full_path = f"{base_path}/{filename}"

        with open(full_path, "w") as f:
            json.dump(scene_dict, f, indent=4)

    @classmethod
    def clear_object(cls, obj):
        """Clean up and remove a single object from the scene."""
        # Call on_remove for all components
        for comp in obj.components.values():
            if hasattr(comp, "on_remove"):
                comp.on_remove()

        # Clear components and owner reference
        obj.components.clear()
        obj.owner = None

        # Remove from list if still exists
        if obj in cls.objects:
            cls.objects.remove(obj)

    @classmethod
    def clear_all_objects(cls):
        """Clear all objects from the scene safely."""
        for obj in list(cls.objects):  # iterate over a copy
            cls.clear_object(obj)

        cls.objects.clear()
        cls.main_camera = None

    @classmethod
    def reset_scene(cls):
        Scene.clear_all_objects()
        from Systems.system_scene_loader import load_scene
        load_scene(Scene.active_scene_file)

    @classmethod
    def update(cls):
        for obj in cls.objects:
            if hasattr(obj, "update"):
                obj.update()
