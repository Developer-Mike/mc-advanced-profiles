import os
from utils.mod import Mod
from typing import List

class AdvancedProfileHelper:
    _ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
    ADVANCED_PROFILES_PATH = os.path.join(_ROOT_PATH, "config", "profiles")
    DEFAULT_PROFILE_PATH = os.path.join(_ROOT_PATH, "config", "default_profile")
    
    def get_profile_mod_paths(self, profile_id: str) -> List[str]:
        mods_path = os.path.join(AdvancedProfileHelper.ADVANCED_PROFILES_PATH, profile_id, "mods")

        if not os.path.exists(mods_path): return None
        else: return [os.path.join(mods_path, mod_path) for mod_path in os.listdir(mods_path) if mod_path.endswith(".jar")]

    def get_profile_mods(self, profile_id: str) -> List[Mod]:
        mod_paths = self.get_profile_mod_paths(profile_id)

        if mod_paths is None: return None
        else: return [Mod(mod_path) for mod_path in mod_paths]