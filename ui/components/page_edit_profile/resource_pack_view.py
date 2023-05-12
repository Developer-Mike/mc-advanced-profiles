import customtkinter as ctk
import tkinter as tk

from utils.assets import DELETE_ICON_WHITE

from ui.components.image_button import ImageButton
from ui.components.image_view import ImageView
from ui.components.themed_components import ThemedLabel

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ui.app import App
    from utils.resource_pack import ResourcePack

class ResourcePackView(ctk.CTkFrame):
    def __init__(self, app: "App", root, resource_pack: "ResourcePack", delete_callback: callable):
        super().__init__(root)
        self.app = app
        self.root = root
        self.resource_pack = resource_pack

        lb_icon = ImageView(self, resource_pack.icon, size=(75, 75), radius=20)
        lb_icon.pack(side=tk.LEFT, anchor="nw", padx=10, pady=10)

        fv_content = ctk.CTkFrame(self, fg_color="transparent")
        fv_content.pack(padx=(10, 75), pady=15, fill="both", expand=True)

        fv_name = ctk.CTkFrame(fv_content, fg_color="transparent")
        fv_name.pack(side=tk.TOP, anchor="nw", fill="x")

        lb_name = ThemedLabel(fv_name, text=resource_pack.filename[:-4], font_size=20, bold=True)
        lb_name.pack(side=tk.LEFT, anchor="nw")

        lb_rp_description = ThemedLabel(fv_content, text=resource_pack.description, font_size=15, text_color="#aaaaaa")
        lb_rp_description.pack(side=tk.BOTTOM, anchor="sw")

        bt_delete = ImageButton(self, image=DELETE_ICON_WHITE, size=(30, 30), transparent=True, command=lambda: delete_callback(resource_pack))
        bt_delete.place(relx=1, rely=0.5, anchor="center", x=-30, y=0)