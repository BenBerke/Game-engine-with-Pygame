import os
import importlib.util
import inspect

def load_custom_behaviours(base_folder="Assets"):
    behaviours = {}

    for root, _, files in os.walk(base_folder):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                file_path = os.path.join(root, file)
                module_name = file_path.replace(os.sep, ".")[:-3]  # convert path to module name

                try:
                    # Dynamically import the module
                    spec = importlib.util.spec_from_file_location(module_name, file_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    # Find all CustomBehaviour subclasses
                    from Classes.class_custom_behaviour import CustomBehaviour
                    for name, obj in inspect.getmembers(module, inspect.isclass):
                        if issubclass(obj, CustomBehaviour) and obj is not CustomBehaviour:
                            behaviours[name] = obj
                            print(f"[CustomBehaviour] Loaded: {name} from {module_name}")

                except Exception as e:
                    print(f"[Error] Failed to import {module_name}: {e}")

    return behaviours
