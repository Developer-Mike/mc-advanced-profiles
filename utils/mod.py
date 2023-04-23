import os, json, zipfile, base64

class ModType:
    FORGE = "forge"
    FABRIC = "fabric"

class Mod:
    def __init__(self, mod_path: str) -> None:
        self.mod_path = mod_path
        self.mod_id = None
        self.mod_icon = None
        self.mod_name = os.path.basename(mod_path)
        self.mod_description = None
        self.mod_version = None
        self.mod_type = None
        self.mod_minecraft_version = None
        self.mod_dependencies = {}

        with zipfile.ZipFile(mod_path, 'r') as zf:
            content = zf.infolist()
            filenames = [file_info.filename for file_info in content]

            if "fabric.mod.json" in filenames:
                self.mod_type = ModType.FABRIC
            elif "mcmod.info" in filenames:
                self.mod_type = ModType.FORGE

            if self.mod_type == ModType.FORGE:
                with zf.open("mcmod.info") as f:
                    config_json = json.load(f)[0]

                    self.mod_id = config_json["modid"]
                    self.mod_name = config_json["name"]
                    self.mod_description = config_json["description"]
                    self.mod_version = config_json["version"]
                    self.mod_minecraft_version = config_json["mcversion"]
                    self.mod_dependencies = config_json["requiredMods"]

                    mod_icon_path = config_json["logoFile"]
                    if mod_icon_path is not None:
                        with zf.open(mod_icon_path) as f:
                            self.mod_icon = base64.b64encode(f.read())


            elif self.mod_type == ModType.FABRIC:
                with zf.open("fabric.mod.json") as f:
                    config_json = json.load(f)

                    self.mod_id = config_json["id"]
                    self.mod_name = config_json["name"]
                    self.mod_description = config_json["description"]
                    self.mod_version = config_json["version"]
                    self.mod_minecraft_version = config_json["depends"]["minecraft"]
                    self.mod_dependencies = [dependency for dependency in config_json["depends"] if dependency not in ["minecraft", "fabricloader", "fabric"]]

                    mod_icon_path = config_json["icon"]
                    if mod_icon_path is not None:
                        with zf.open(mod_icon_path) as f:
                            self.mod_icon = base64.b64encode(f.read())