import customtkinter as ctk
from ui.app import App

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = App()
app.geometry("1000x550")
app.minsize(1000, 550)

app.mainloop()