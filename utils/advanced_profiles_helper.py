import os, json, shutil
from utils.mod import Mod
from typing import List

class AdvancedProfileHelper:
    _ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
    ADVANCED_PROFILES_PATH = os.path.join(_ROOT_PATH, "config", "profiles")
    DEFAULT_PROFILE_PATH = os.path.join(_ROOT_PATH, "config", "default_profile")

    def _get_default_config(self) -> dict:
        return {
            "server": None,
            "resource_packs": [],
        }
    
    def _modify_profile_config(self, profile_id: str, key: str, value: any):
        profile_config = self._get_profile_config(profile_id)
        profile_config[key] = value

        config_path = os.path.join(AdvancedProfileHelper.ADVANCED_PROFILES_PATH, profile_id, "config.json")
        with open(config_path, "w") as f:
            json.dump(profile_config, f, indent=4)

    def _get_profile_config(self, profile_id: str) -> dict:
        config_path = os.path.join(AdvancedProfileHelper.ADVANCED_PROFILES_PATH, profile_id, "config.json")

        if not os.path.exists(config_path): return self._get_default_config()
        with open(config_path, "r") as f:
            return json.load(f)

    def add_profile_mods(self, profile_id: str, mods: List[Mod]):
        mods_path = os.path.join(AdvancedProfileHelper.ADVANCED_PROFILES_PATH, profile_id, "mods")

        if not os.path.exists(mods_path): os.makedirs(mods_path)
        for mod in mods:
            target_mod_path = os.path.join(mods_path, os.path.basename(mod.path))
            shutil.copy(mod.path, target_mod_path)
    
    def get_profile_mod_paths(self, profile_id: str) -> List[str]:
        mods_path = os.path.join(AdvancedProfileHelper.ADVANCED_PROFILES_PATH, profile_id, "mods")

        if not os.path.exists(mods_path): return None
        else: return [os.path.join(mods_path, mod_path) for mod_path in os.listdir(mods_path) if mod_path.endswith(".jar")]

    def get_profile_mods(self, profile_id: str) -> List[Mod]:
        mod_paths = self.get_profile_mod_paths(profile_id)

        if mod_paths is None: return None
        else: return [Mod(mod_path) for mod_path in mod_paths]

    def set_profile_server(self, profile_id: str, server: str):
        self._modify_profile_config(profile_id, "server", server)

    def get_profile_server(self, profile_id: str) -> str:
        profile_config = self._get_profile_config(profile_id)
        return profile_config["server"]
    
    def set_profile_resource_packs(self, profile_id: str, resource_packs: List[str]):
        self._modify_profile_config(profile_id, "resource_packs", resource_packs)

    def get_profile_resource_packs(self, profile_id: str) -> List[str]:
        profile_config = self._get_profile_config(profile_id)
        return profile_config["resource_packs"]