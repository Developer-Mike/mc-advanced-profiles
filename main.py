import customtkinter as ctk
from ui.app import App

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = App()
app.geometry("1000x550")
app.minsize(1000, 550)

# DEBUG
'''
import os

def restart(e):
    if e.keysym == "F5":
        app.destroy()
        os.system(f'cmd /k "python {__file__} -B"')
app.bind("<KeyRelease>", restart)

from ui.page_edit_profile import PageEditProfile
app.navigate(PageEditProfile)
'''

app.mainloop()