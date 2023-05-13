import os, json, zipfile
from io import BytesIO
from PIL import Image

class ModType:
    FORGE = "Forge"
    FABRIC = "Fabric"

class Mod:
    def __init__(self, mod_path: str) -> None:
        self.path = mod_path
        self.id = ""
        self.icon = None
        self.mod_name = os.path.basename(mod_path).split(".")[0]
        self.description = ""
        self.version = None
        self.client_type = None
        self.minecraft_version = ["*"]
        self.dependencies = {}

        with zipfile.ZipFile(mod_path, 'r') as zf:
            content = zf.infolist()
            filenames = [file_info.filename for file_info in content]

            if "fabric.mod.json" in filenames:
                self.client_type = ModType.FABRIC
            elif "mcmod.info" in filenames:
                self.client_type = ModType.FORGE

            if self.client_type == ModType.FORGE:
                with zf.open("mcmod.info") as f:
                    config_json = json.load(f)[0]

                    self.id = config_json["modid"]
                    self.mod_name = config_json["name"]
                    self.description = config_json["description"]
                    self.version = config_json["version"]
                    self.minecraft_version = [config_json["mcversion"]]
                    self.dependencies = config_json.get("requiredMods") or []

                    mod_icon_path = config_json.get("logoFile")
                    if mod_icon_path is not None and mod_icon_path != "":
                        with zf.open(mod_icon_path) as f:
                            self.icon = Image.open(f)


            elif self.client_type == ModType.FABRIC:
                with zf.open("fabric.mod.json") as f:
                    config_json = json.load(f)

                    self.id = config_json["id"]
                    self.mod_name = config_json["name"]
                    self.description = config_json["description"]
                    self.version = config_json["version"]

                    minecraft_version = config_json["depends"].get("minecraft")
                    if minecraft_version is None: self.minecraft_version = ["*"]
                    elif isinstance(minecraft_version, list): self.minecraft_version = minecraft_version
                    else: self.minecraft_version = minecraft_version.split(" ")

                    self.dependencies = [dependency for dependency in config_json["depends"] if dependency not in ["minecraft", "fabricloader", "fabric"]]

                    mod_icon_path = config_json.get("icon")
                    if mod_icon_path is not None:
                        with zf.open(mod_icon_path) as f:
                            self.icon = Image.open(BytesIO(f.read()))
    
    def compatible_with(self, minecraft_version: str) -> bool:
        to_numeric = lambda version: int("".join([version.zfill(3) for version in version.split(".")]))
        minecraft_version = to_numeric(minecraft_version)

        for version in self.minecraft_version:
            if version == "*":
                return True
        
            version_start_index = [i for i, char in enumerate(version) if char.isdigit()][0]

            version_prefix = version[:version_start_index]
            version = version[version_start_index:]
            numeric_version = to_numeric(version)
        
            if version_prefix.startswith("="):
                if minecraft_version == numeric_version:
                    return True
            elif version_prefix.startswith(">"):
                if minecraft_version > numeric_version:
                    return True
            elif version_prefix.startswith("<"):
                if minecraft_version < numeric_version:
                    return True
            elif version_prefix.startswith("<=") or version_prefix.startswith("=<"):
                if minecraft_version <= numeric_version:
                    return True
            elif version_prefix.startswith(">=") or version_prefix.startswith("=>"):
                if minecraft_version >= numeric_version:
                    return True
            elif version_prefix.startswith("^"):
                if minecraft_version >= numeric_version and minecraft_version < (numeric_version + 1000000):
                    return True
            elif version_prefix.startswith("~"):
                if minecraft_version >= numeric_version and minecraft_version < (numeric_version + 1000):
                    return True
                
        return False
    
    def __eq__(self, __value: object) -> bool:
        return self.path == __value.path