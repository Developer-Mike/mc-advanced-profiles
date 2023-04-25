import os, json, shutil
from utils.mod import Mod
from typing import List

class AdvancedProfileHelper:
    _ROOT_PATH = os.path.dirname(os.path.dirname(__file__))
    ADVANCED_PROFILES_PATH = os.path.join(_ROOT_PATH, "config", "profiles")
    DEFAULT_PROFILE_PATH = os.path.join(_ROOT_PATH, "config", "default_profile")

    def _get_profile_path(self, profile_id: str) -> str:
        if profile_id is not None: return os.path.join(AdvancedProfileHelper.ADVANCED_PROFILES_PATH, profile_id)
        else: return os.path.join(AdvancedProfileHelper.DEFAULT_PROFILE_PATH)

    def _get_default_config(self) -> dict:
        return {
            "server": None,
            "resource_packs": [],
        }
    
    def _modify_profile_config(self, profile_id: str, key: str, value: any):
        profile_config = self._get_profile_config(profile_id)
        profile_config[key] = value

        config_path = os.path.join(self._get_profile_path(profile_id), "config.json")

        with open(config_path, "w") as f:
            json.dump(profile_config, f, indent=4)

    def _get_profile_config(self, profile_id: str) -> dict:
        config_path = os.path.join(self._get_profile_path(profile_id), "config.json")

        if not os.path.exists(config_path): return self._get_default_config()
        with open(config_path, "r") as f:
            return json.load(f)

    def add_profile_mods(self, profile_id: str, mods: List[Mod]):
        mods_path = os.path.join(self._get_profile_path(profile_id), "mods")

        if not os.path.exists(mods_path): os.makedirs(mods_path)
        for mod in mods:
            target_mod_path = os.path.join(mods_path, os.path.basename(mod.path))
            shutil.copy(mod.path, target_mod_path)
    
    def get_profile_mod_paths(self, profile_id: str) -> List[str]:
        mods_path = os.path.join(self._get_profile_path(profile_id), "mods")

        if not os.path.exists(mods_path): return None
        else: return [os.path.join(mods_path, mod_path) for mod_path in os.listdir(mods_path) if mod_path.endswith(".jar")]

    def get_profile_mods(self, profile_id: str) -> List[Mod]:
        mod_paths = self.get_profile_mod_paths(profile_id)

        if mod_paths is None: return None
        else: return [Mod(mod_path) for mod_path in mod_paths]

    def set_profile_quickplay_server(self, profile_id: str, server: str):
        self._modify_profile_config(profile_id, "direct_play_server", server)

    def get_profile_quickplay_server(self, profile_id: str) -> str:
        profile_config = self._get_profile_config(profile_id)
        return profile_config["direct_play_server"]
    
    def set_profile_resource_packs(self, profile_id: str, resource_packs: List[str]):
        self._modify_profile_config(profile_id, "resource_packs", resource_packs)

    def get_profile_resource_packs(self, profile_id: str) -> List[str]:
        profile_config = self._get_profile_config(profile_id)
        return profile_config["resource_packs"]

    def _set_options_txt_resource_packs(self, mc_path: str, resource_packs: List[str]) -> List[str]:
        new_resource_packs_strings = [f'"{resource_pack}"' for resource_pack in resource_packs]
        new_resource_packs = f"[{','.join(new_resource_packs_strings)}]"

        options_txt_path = os.path.join(mc_path, "options.txt")
        with open(options_txt_path, "r") as f:
            options_txt = f.readlines()

        old_resource_packs = None
        for i, line in enumerate(options_txt):
            if line.startswith("resourcePacks:"):
                old_resource_packs = line.replace("resourcePacks:[", "").replace("]", "").replace("\n", "").replace('"', "").split(",")

                options_txt[i] = f"resourcePacks:{new_resource_packs}\n"
                break

        with open(options_txt_path, "w") as f:
            f.write("".join(options_txt))

        return old_resource_packs

    def initialize_profile(self, mc_path: str, profile_id: str):
        if profile_id is None: return
        profile_path = self._get_profile_path(profile_id)
        if not os.path.exists(profile_path): return

        mc_mod_folder = os.path.join(mc_path, "mods")

        default_profile_mods_path = os.path.join(AdvancedProfileHelper.DEFAULT_PROFILE_PATH, "mods")
        if not os.path.exists(default_profile_mods_path): os.makedirs(default_profile_mods_path)

        # Move all mods from the mods folder to the default profile's mods folder
        for relative_mod_path in os.listdir(mc_mod_folder):
            if not relative_mod_path.endswith(".jar"): continue
            shutil.move(os.path.join(mc_mod_folder, relative_mod_path), default_profile_mods_path)

        # Move all mods from the profile's mods folder to the mods folder
        for mod_path in self.get_profile_mod_paths(profile_id):
            if not mod_path.endswith(".jar"): continue
            shutil.copy(mod_path, os.path.join(mc_mod_folder, os.path.basename(mod_path)))

        # Get and replace the default active resource packs
        new_resource_packs = self.get_profile_resource_packs(profile_id)
        old_resource_packs = self._set_options_txt_resource_packs(mc_path, new_resource_packs)
        self.set_profile_resource_packs(None, old_resource_packs)

    def restore_default_profile(self, mc_path: str):
        mc_mod_folder = os.path.join(mc_path, "mods")
        for relative_mod_path in os.listdir(mc_mod_folder):
            if not relative_mod_path.endswith(".jar"): continue
            os.remove(os.path.join(mc_mod_folder, relative_mod_path))

        default_profile_mods_path = self.get_profile_mod_paths(None)
        for mod_path in default_profile_mods_path:
            if not mod_path.endswith(".jar"): continue
            shutil.move(mod_path, os.path.join(mc_mod_folder, os.path.basename(mod_path)))

        self._set_options_txt_resource_packs(mc_path, self.get_profile_resource_packs(None))