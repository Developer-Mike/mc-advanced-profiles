import os, json

class Settings:
    SETTINGS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "settings.json")

    def __init__(self) -> None:
        if os.path.exists(Settings.SETTINGS_PATH):
            self.settings = json.load(open(Settings.SETTINGS_PATH, 'r'))
        else:
            print("Settings file not found at " + Settings.SETTINGS_PATH)
            self.settings = {}

    def get(self, key) -> str:
        if key not in self.settings:
            return None
        else:
            return self.settings[key]