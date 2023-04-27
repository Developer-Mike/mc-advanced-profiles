import tkinter as tk
import customtkinter as ctk
from ui.components.image_button import ImageButton
from ui.components.page_profiles_list.profiles_list import ProfilesList
from utils.assets import PLUS_ICON_WHITE

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ui.app import App

class PageProfilesList(ctk.CTkFrame):
    def __init__(self, app: "App"):
        super().__init__(app, fg_color="transparent")
        self.app = app

        fv_content = ctk.CTkScrollableFrame(self, fg_color="transparent")

        lb_title = ctk.CTkLabel(fv_content, text="Profiles", font=("Arial", 30, "bold"))
        lb_title.pack(side=tk.TOP, anchor="nw", padx=40, pady=40)
        
        fv_profiles = ProfilesList(self.app, fv_content, self.app.mc_profile_helper.get_profiles())
        fv_profiles.pack(side=tk.TOP, fill="both", expand=True, padx=40, pady=(0, 50))

        fv_content.pack(side=tk.TOP, fill="both", expand=True)

        bt_create_profile = ImageButton(self, PLUS_ICON_WHITE, size=(75, 75), padding=(30, 30), command=self._create_profile)
        bt_create_profile.place(relx=1, rely=1, anchor="se", x=-40, y=-40)

    def _create_profile(self):
        from ui.page_edit_profile import PageEditProfile
        self.app.navigate(PageEditProfile)