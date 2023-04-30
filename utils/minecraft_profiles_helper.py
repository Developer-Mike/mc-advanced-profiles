import json, os
from PIL import Image
from io import BytesIO
import base64
from typing import List

PROFILE_ID_PREFIX = "multiprofile-"

class MCProfile:
    def __init__(self, profile_id: str, profile_icon: str, profile_name: str, version_id: str) -> None:
        self.profile_id = profile_id
        self.profile_icon = profile_icon
        self.profile_name = profile_name
        self.version_id = version_id

    def get_icon(self) -> Image:
        if self.profile_icon is None: return None
        else: return Image.open(BytesIO(base64.b64decode(self.profile_icon.split(",")[-1])))

class MCProfileHelper:
    LAUNCHER_PROFILES_RELATIVE_PATH = "launcher_profiles.json"

    # Should default to C:\Users\%USERNAME%\AppData\Roaming\.minecraft
    def __init__(self, mc_path: str) -> None:
        self.mc_path = os.path.join(mc_path, MCProfileHelper.LAUNCHER_PROFILES_RELATIVE_PATH)

    def get_profiles(self, ignore_others = True) -> List[MCProfile]:
        with open(self.mc_path, "r") as f:
            profiles_json = json.load(f)["profiles"]

        profiles = [MCProfile(profile_id, profile["icon"], profile["name"], profile["lastVersionId"]) for profile_id, profile in profiles_json.items()]
        if not ignore_others: return profiles
        else: return [profile for profile in profiles if profile.profile_id.startswith(PROFILE_ID_PREFIX)]
    
    def _set_profile(self, profile: MCProfile) -> None:
        with open(self.mc_path, "r") as f:
            file = json.load(f)

        file["profiles"][profile.profile_id] = {
            "name": profile.profile_name,
            "type": "custom",
            "gameDir": self.mc_path,
            "lastVersionId": profile.version_id
        }

        with open(self.mc_path, "w") as f:
            json.dump(file, f, indent=4)

    def remove_profile(self, profile_id: str) -> None:
        with open(self.mc_path, "r") as f:
            file = json.load(f)

        file["profiles"].pop(profile_id)

        with open(self.mc_path, "w") as f:
            json.dump(file, f, indent=4)