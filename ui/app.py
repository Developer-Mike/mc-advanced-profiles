import tkinter as tk
import customtkinter as ctk
import os

from utils.settings_helper import SettingsHelper
from utils.minecraft_profiles_helper import MCProfileHelper
from utils.advanced_profiles_helper import AdvancedProfileHelper

from ui.page_profiles_list import PageProfilesList
from ui.page_create_profile import PageCreateProfile

class App(ctk.CTk):
    _ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

    def __init__(self):
        super().__init__()
        self.title("Advanced Profiles")
        self.iconbitmap(os.path.join(self._ROOT_DIR, "assets", "icon.ico"))

        self.settings_helper = SettingsHelper()
        self.mc_profile_helper = MCProfileHelper(self.settings_helper.get("minecraft_path"))
        self.advanced_profile_helper = AdvancedProfileHelper()

        self.pages = [
            PageProfilesList(self),
            PageCreateProfile(self),
        ]

        self.navigate(self.pages[0])

    def navigate(self, page):
        for other_page in self.pages:
            other_page.pack_forget()

        page.pack(expand=True, fill="both")
        page.update()
