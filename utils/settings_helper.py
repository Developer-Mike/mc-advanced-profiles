import os, json

class SettingsHelper:
    SETTINGS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "settings.json")

    def __init__(self) -> None:
        if os.path.exists(SettingsHelper.SETTINGS_PATH):
            self.settings = json.load(open(SettingsHelper.SETTINGS_PATH, 'r'))
        else:
            self.settings = {}
            self._generate_default_settings()

    def get(self, key) -> str:
        if key not in self.settings: return None
        else: return self.settings[key]
        
    def set(self, key, value) -> None:
        self.settings[key] = value

        if not os.path.exists(os.path.dirname(SettingsHelper.SETTINGS_PATH)):
            os.makedirs(os.path.dirname(SettingsHelper.SETTINGS_PATH))
        json.dump(self.settings, open(SettingsHelper.SETTINGS_PATH, 'w'))
        
    def _generate_default_settings(self) -> dict:
        self.set("minecraft_path", f"C:/Users/{os.getlogin()}/AppData/Roaming/.minecraft")
        self.set("java_path", os.join(os.getenv("JAVA_HOME"), "/bin/java.exe"))