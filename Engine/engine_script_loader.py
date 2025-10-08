import os
import importlib.util
import inspect

def load_custom_behaviours(assets_folder="Assets"):
    behaviours = {}

    for root, _, files in os.walk(assets_folder):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                module_name = os.path.splitext(os.path.relpath(path, assets_folder))[0].replace(os.sep, ".")

                spec = importlib.util.spec_from_file_location(module_name, path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Find all CustomBehaviour subclasses in the module
                from Classes import CustomBehaviour
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if issubclass(obj, CustomBehaviour) and obj is not CustomBehaviour:
                        behaviours[name] = obj

    return behaviours
