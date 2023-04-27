import tkinter as tk
import customtkinter as ctk

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ui.app import App
    from utils.minecraft_profiles_helper import MCProfile

class PageEditProfile(ctk.CTkFrame):
    def __init__(self, app: "App", profile: "MCProfile" = None):
        super().__init__(app, fg_color="transparent")
        self.app = app

        ctk.CTkLabel(self, text="Create Profile").pack()
        ctk.CTkButton(self, text="Back", command=self._back).pack()

    def _back(self):
        from ui.page_profiles_list import PageProfilesList
        self.app.navigate(PageProfilesList)