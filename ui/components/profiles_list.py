import customtkinter as ctk
import tkinter as tk

from typing import TYPE_CHECKING

from ui.components.image_view import ImageView
if TYPE_CHECKING:
    from ui.app import App
    from utils.minecraft_profiles_helper import MCProfile

class ProfileView(ctk.CTkFrame):
    def __init__(self, app: "App", root, profile: "MCProfile"):
        super().__init__(root)
        self.app = app
        self.root = root
        self.profile = profile

        lb_icon = ImageView(self, profile.get_icon(), size=(75, 75))
        lb_icon.pack(side=tk.LEFT, anchor="nw", padx=10, pady=10)

        lb_name = ctk.CTkLabel(self, text=profile.profile_name, font=("Arial", 20, "bold"))
        lb_name.pack(side=tk.LEFT, anchor="nw", padx=10, pady=10)

class ProfilesList(ctk.CTkFrame):
    def __init__(self, app: "App", root):
        super().__init__(root, fg_color="transparent")
        self.app = app
        self.root = root

        self.profiles = []
        self.profile_views = []

        self.update()

    def update(self) -> None:
        # Clear the profiles list
        for profile_view in self.profile_views:
            profile_view.destroy()

        self.profile_views = []

        # Add the profiles
        for profile in self.profiles:
            profile_view = ProfileView(self.app, self, profile)
            profile_view.pack(side=tk.TOP, fill="x", pady=5)
            self.profile_views.append(profile_view)

        return super().update()
