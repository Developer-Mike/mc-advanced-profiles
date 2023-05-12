import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import os

from utils.assets import PLUS_ICON_WHITE
from utils.resource_pack import ResourcePack

from ui.components.image_button import ImageButton
from ui.components.themed_components import ThemedLabel
from ui.components.page_edit_profile.resource_pack_view import ResourcePackView

from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from ui.app import App

class ResourcePackSelection(ctk.CTkFrame):
    def __init__(self, root: any, app: "App", resource_packs: List[ResourcePack], **kwargs):
        kwargs["fg_color"] = "transparent"
        super().__init__(root, **kwargs)

        self.app = app

        lb_resource_packs = ThemedLabel(self, text="Resource Packs", font_size=30, bold=True)
        lb_resource_packs.pack(side=tk.LEFT, anchor="nw", pady=10)

        bt_add_resource_pack = ImageButton(self, PLUS_ICON_WHITE, size=(25, 25), padding=(5, 5), command=self._add_resource_pack_dialog)
        bt_add_resource_pack.pack(side=tk.LEFT, anchor="nw", padx=20, pady=10)

        self.fv_resource_packs = ctk.CTkFrame(self, fg_color="transparent")
        self.resource_packs = []
        self._fill_resource_pack_list(resource_packs)
        self.fv_resource_packs.pack(side=tk.TOP, anchor="nw", padx=20, pady=10, fill="both", expand=True)

    def _fill_resource_pack_list(self, resource_packs: List[ResourcePack]):
        for resource_pack in resource_packs:
            self._add_resource_pack(resource_pack)

    def _add_resource_pack_dialog(self):
        rp_folder_path = os.path.join(self.app.settings_helper.get("minecraft_path"), "resourcepacks")
        resource_pack_paths = filedialog.askopenfilenames(initialdir=rp_folder_path, filetypes=[("Resource Pack", "*.zip")])

        for resource_pack_path in resource_pack_paths:
            if os.path.normpath(rp_folder_path) not in os.path.normpath(resource_pack_path):
                continue
            
            resource_pack = ResourcePack(resource_pack_path)
            if resource_pack.is_valid and resource_pack not in self.resource_packs:
                self._add_resource_pack(resource_pack)

    def _add_resource_pack(self, resource_pack: ResourcePack):
        if resource_pack not in self.resource_packs:
            self.resource_packs.append(resource_pack)

        resource_pack_view = ResourcePackView(self.app, self.fv_resource_packs, resource_pack, self._delete_resource_pack)
        resource_pack_view.pack(pady=5, fill="x")

    def _delete_resource_pack(self, resource_pack: ResourcePack):
        self.resource_packs.remove(resource_pack)
        
        for widget in self.fv_resource_packs.winfo_children():
            widget.destroy()

        self._fill_resource_pack_list(self.resource_packs)