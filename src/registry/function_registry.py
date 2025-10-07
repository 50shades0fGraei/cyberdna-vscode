import json
from datetime import datetime

class FunctionRegistry:
    def __init__(self, registry_path="function_registry.json"):
        self.registry_path = registry_path
        self.functions = self.load_registry()

    def load_registry(self):
        try:
            with open(self.registry_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_registry(self):
        with open(self.registry_path, "w") as f:
            json.dump(self.functions, f, indent=2)

    def add_function(self, segment_id, title, code, traits=None):
        self.functions[segment_id] = {
            "title": title,
            "code": code,
            "traits": traits or [],
            "createdAt": datetime.utcnow().isoformat(),
            "editable": True
        }
        self.save_registry()

    def summon(self, segment_id):
        return self.functions.get(segment_id)

    def edit_function(self, segment_id, new_code):
        if segment_id in self.functions and self.functions[segment_id]["editable"]:
            self.functions[segment_id]["code"] = new_code
            self.save_registry()

    def list_functions(self):
        return {k: v["title"] for k, v in self.functions.items()}

