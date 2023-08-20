import os, json, zipfile
from PIL import Image

class ResourcePack:
    def __init__(self, resource_pack_path: str) -> None:
        self.path = resource_pack_path
        self.filename = os.path.basename(resource_pack_path)
        self.description = ""
        self.icon = None
        self.is_valid = True

        with zipfile.ZipFile(resource_pack_path, 'r') as zf:
            if "pack.mcmeta" not in zf.namelist():
                self.is_valid = False
                return
            
            try:
                with zf.open("pack.mcmeta") as f:
                    config_json = json.load(f)["pack"]
                    self.description = config_json["description"]
            except:
                pass

            try:
                with zf.open("pack.png") as f:
                    self.icon = Image.open(f).copy()
            except:
                pass

    def __eq__(self, __value: object) -> bool:
        return self.path == __value.path