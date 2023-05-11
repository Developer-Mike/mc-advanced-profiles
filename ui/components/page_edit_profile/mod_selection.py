import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import os

from utils.mod import Mod
from utils.assets import PLUS_ICON_WHITE

from ui.components.image_button import ImageButton
from ui.components.themed_components import ThemedLabel
from ui.components.page_edit_profile.mod_view import ModView

from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from ui.app import App

class ModSelection(ctk.CTkFrame):
    def __init__(self, root: any, app: "App", mods: List[Mod], **kwargs):
        kwargs["fg_color"] = "transparent"
        super().__init__(root, **kwargs)

        self.app = app

        lb_mods = ThemedLabel(self, text="Mods", font_size=30, bold=True)
        lb_mods.pack(side=tk.LEFT, anchor="nw", pady=10)

        bt_add_mod = ImageButton(self, PLUS_ICON_WHITE, size=(25, 25), padding=(5, 5), command=self._add_mod_dialog)
        bt_add_mod.pack(side=tk.LEFT, anchor="nw", padx=20, pady=10)

        self.fv_mods = ctk.CTkFrame(self, fg_color="transparent")
        self.mods = []
        self._fill_mod_list(mods or [])
        self.fv_mods.pack(side=tk.TOP, anchor="nw", padx=20, pady=10, fill="both", expand=True)

    def _fill_mod_list(self, mods: List[Mod]):
        for mod in mods:
            self._add_mod(mod)

    def _add_mod_dialog(self):
        mods_folder_path = os.path.join(self.app.settings_helper.get("minecraft_path"), "mods")
        mod_paths = filedialog.askopenfilenames(initialdir=mods_folder_path, filetypes=[("Mod", "*.jar")])

        for mod_path in mod_paths:
            mod = Mod(mod_path)

            if mod not in self.mods:
                self._add_mod(mod)

    def _add_mod(self, mod: Mod):
        if mod not in self.mods:
            self.mods.append(mod)

        mod_view = ModView(self.app, self.fv_mods, mod, self._delete_mod)
        mod_view.pack(pady=5, fill="x")

    def _delete_mod(self, mod: Mod):
        self.mods.remove(mod)
        
        for widget in self.fv_mods.winfo_children():
            widget.destroy()

        self._fill_mod_list(self.mods)