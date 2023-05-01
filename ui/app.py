import tkinter as tk
import customtkinter as ctk
import os

from utils.settings_helper import SettingsHelper
from utils.minecraft_profiles_helper import MCProfileHelper
from utils.advanced_profiles_helper import AdvancedProfileHelper

from ui.page_profiles_list import PageProfilesList

class App(ctk.CTk):
    ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

    def __init__(self):
        super().__init__()
        self.title("Advanced Profiles")
        self.iconbitmap(os.path.join(self.ROOT_DIR, "assets", "icon.ico"))

        self.settings_helper = SettingsHelper()
        self.mc_profile_helper = MCProfileHelper(self.settings_helper.get("minecraft_path"))
        self.advanced_profile_helper = AdvancedProfileHelper()

        self.active_page = None
        self.navigate(PageProfilesList)

    def navigate(self, page, **kwargs):
        if self.active_page is not None:
            self.active_page.destroy()

        self.active_page = page(self, **kwargs)
        self.active_page.pack(expand=True, fill="both")