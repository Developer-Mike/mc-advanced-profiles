import customtkinter as ctk
from ui.app import App

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = App()
app.geometry("1000x550")

app.mainloop()

'''
from utils.settings_helper import SettingsHelper
from utils.minecraft_profiles_helper import MCProfileHelper
from utils.advanced_profiles_helper import AdvancedProfileHelper

settings_helper = SettingsHelper()
minecraft_path = settings_helper.get("minecraft_path")

profiles_helper = MCProfileHelper(minecraft_path)
advanced_profiles_helper = AdvancedProfileHelper()
'''