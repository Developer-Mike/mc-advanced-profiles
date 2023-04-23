import os
from mod import Mod
from typing import List

class AdvancedProfileHelper:
    ADVANCED_PROFILES_PATH = os.path.join(os.path.dirname(__file__), "config", "profiles")
    DEFAULT_PROFILE_PATH = os.path.join(os.path.dirname(__file__), "config", "default_profile")
    
    def get_profile_mods(self, profile_id: str) -> List[Mod]:
        profile_path = os.path.join(AdvancedProfileHelper.ADVANCED_PROFILES_PATH, profile_id, "mods")

        if not os.path.exists(profile_path): return None
        else:
            files = os.listdir(profile_path)
            return [Mod(os.path.join(profile_path, mod)) for mod in files if mod.endswith(".jar")]