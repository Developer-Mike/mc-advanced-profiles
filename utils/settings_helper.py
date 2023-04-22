import os, json

DEBUG = True

class Settings:
    SETTINGS_RELATIVE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'settings.json') \
        if not DEBUG else \
            os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'settings.json')

    def __init__(self) -> None:
        self.settings = json.load(open(Settings.SETTINGS_RELATIVE_PATH, 'r'))

    def get(self, key) -> str:
        if key not in self.settings:
            return None
        else:
            return self.settings[key]