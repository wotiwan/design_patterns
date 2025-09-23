from rOMASHKA.src.models.company_model import company_model
import json

class load_model_settings:
    def __init__(self):
        self.model = company_model()

    def load_file(self, file_name:str = ""):
        file_name = "D:/учёба/Volovikov/Patterns2025/rOMASHKA/settings.json"
        file = open(file_name, 'r', encoding="utf-8")
        data = json.load(file)
        return data

    def apply_settings(self):
        data = self.load_file()
        item = data["company"]
        self.model.name = item["name"]

if __name__ == "__main__":
    loaded_settings = load_model_settings()
    loaded_settings.apply_settings()
    print(loaded_settings.model.name)