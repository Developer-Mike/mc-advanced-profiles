import customtkinter as ctk
import tkinter as tk

from utils.assets import DELETE_ICON_WHITE

from ui.components.image_button import ImageButton
from ui.components.image_view import ImageView

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ui.app import App
    from utils.minecraft_profiles_helper import MCProfile

class ProfileView(ctk.CTkFrame):
    def __init__(self, app: "App", root, profile: "MCProfile"):
        super().__init__(root)
        self.app = app
        self.root = root
        self.profile = profile

        lb_icon = ImageView(self, profile.get_icon(), size=(75, 75), radius=20)
        lb_icon.pack(side=tk.LEFT, anchor="nw", padx=10, pady=10)

        fv_content = ctk.CTkFrame(self, fg_color="transparent")
        fv_content.pack(padx=10, pady=15, expand=True, fill="both")

        fv_name = ctk.CTkFrame(fv_content, fg_color="transparent")
        fv_name.pack(side=tk.TOP, anchor="nw", fill="x", expand=True)

        lb_name = ctk.CTkLabel(fv_name, text=profile.profile_name, font=("Arial", 20, "bold"))
        lb_name.pack(side=tk.LEFT, anchor="nw")

        lb_id = ctk.CTkLabel(fv_name, text=f"({profile.profile_id})", font=("Arial", 15), text_color="#aaaaaa")
        lb_id.pack(side=tk.LEFT, anchor="w", padx=10)

        mods_count = len(self.app.advanced_profile_helper.get_profile_mod_paths(profile.profile_id) or [])
        resource_packs_count = 0 # TODO: len(self.app.advanced_profile_helper.get_profile_resource_packs(profile.profile_id) or [])
        
        info_content = []
        if mods_count > 0:
            info_content.append(f"{mods_count} Mods")
        if resource_packs_count > 0:
            info_content.append(f"{resource_packs_count} Resource Packs")

        lb_mods_count = ctk.CTkLabel(fv_content, text="  |  ".join(info_content), font=("Arial", 15), text_color="#aaaaaa")
        lb_mods_count.pack(side=tk.BOTTOM, anchor="sw")

        fv_config = ctk.CTkFrame(self, fg_color="transparent")
        fv_config.place(relx=1, rely=0, anchor="ne", x=-30, y=0)

        bt_delete = ImageButton(fv_config, image=DELETE_ICON_WHITE, size=(30, 30), transparent=True)
        bt_delete.place(relx=1, rely=0.25, anchor="e")
