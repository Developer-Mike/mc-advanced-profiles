import tkinter as tk
import customtkinter as ctk

from utils.settings_helper import SettingsHelper
from utils.minecraft_profiles_helper import MCProfileHelper
from utils.advanced_profiles_helper import AdvancedProfileHelper

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x240")

image_file = None
image_view = ctk.CTkLabel(master=app, image=None)

def button_function():
    settings_helper = SettingsHelper()
    minecraft_path = settings_helper.get("minecraft_path")

    profiles_helper = MCProfileHelper(minecraft_path)
    profile_id = profiles_helper.get_profiles()[1].profile_id

    ap_helper = AdvancedProfileHelper()
    mods = ap_helper.get_profile_mods(profile_id)

    mod = mods[0]
    image_file = ctk.CTkImage(light_image=mod.mod_icon, size=(256, 256))
    image_view.configure(image=image_file)

button = ctk.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

image_view.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

app.mainloop()