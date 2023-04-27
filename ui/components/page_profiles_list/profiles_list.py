import customtkinter as ctk
import tkinter as tk

from ui.components.page_profiles_list.profile_view import ProfileView
from utils.minecraft_profiles_helper import MCProfile

from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from ui.app import App

class ProfilesList(ctk.CTkFrame):
    def __init__(self, app: "App", root, profiles: List[MCProfile]):
        super().__init__(root, fg_color="transparent")
        self.app = app
        self.root = root

        for profile in profiles:
            profile_view = ProfileView(self.app, self, profile)
            profile_view.pack(side=tk.TOP, fill="x", pady=5)
