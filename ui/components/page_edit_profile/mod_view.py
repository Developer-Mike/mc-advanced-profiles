import customtkinter as ctk
import tkinter as tk

from utils.assets import DELETE_ICON_WHITE

from ui.components.image_button import ImageButton
from ui.components.image_view import ImageView

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ui.app import App
    from utils.mod import Mod

class ModView(ctk.CTkFrame):
    def __init__(self, app: "App", root, mod: "Mod", delete_callback: callable):
        super().__init__(root)
        self.app = app
        self.root = root
        self.mod = mod

        lb_icon = ImageView(self, mod.mod_icon, size=(75, 75), radius=20)
        lb_icon.pack(side=tk.LEFT, anchor="nw", padx=10, pady=10)

        fv_content = ctk.CTkFrame(self, fg_color="transparent")
        fv_content.pack(padx=10, pady=15, fill="both")

        fv_name = ctk.CTkFrame(fv_content, fg_color="transparent")
        fv_name.pack(side=tk.TOP, anchor="nw", fill="x")

        lb_name = ctk.CTkLabel(fv_name, text=mod.mod_name, font=("Arial", 20, "bold"))
        lb_name.pack(side=tk.LEFT, anchor="nw")

        lb_id = ctk.CTkLabel(fv_name, text=f"({', '.join(mod.mod_minecraft_version)})", font=("Arial", 15), text_color="#aaaaaa")
        lb_id.pack(side=tk.LEFT, anchor="w", padx=10)

        lb_mods_count = ctk.CTkLabel(fv_content, text=mod.mod_description, font=("Arial", 15), text_color="#aaaaaa")
        lb_mods_count.pack(side=tk.BOTTOM, anchor="sw")

        bt_delete = ImageButton(self, image=DELETE_ICON_WHITE, size=(30, 30), transparent=True, command=lambda: delete_callback(mod))
        bt_delete.place(relx=1, rely=0.5, anchor="center", x=-30, y=0)