import customtkinter as ctk
import tkinter as tk

from ui.components.page_profiles_list.profile_view import ProfileView

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ui.app import App

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
