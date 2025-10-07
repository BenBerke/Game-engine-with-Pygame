import json

class Scene:
    objects = []

    main_camera = None

    @classmethod
    def register_object(cls, obj):
        cls.objects.append(obj)

    @classmethod
    def remove_object(cls, obj):
        if obj in cls.objects:
            cls.objects.remove(obj)

    @classmethod
    def save_scene(cls, filename):
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

        with open(filename, "w") as f:
            json.dump(scene_dict, f, indent=4)

    @classmethod
    def update(cls):
        for obj in cls.objects:
            if hasattr(obj, "update"):
                obj.update()
