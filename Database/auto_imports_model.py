import os
import importlib

def import_all_models():
    model_dir = os.path.join(os.path.dirname(__file__), '../Model')
    for filename in os.listdir(model_dir):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = f"Model.{filename[:-3]}"
            importlib.import_module(module_name)
