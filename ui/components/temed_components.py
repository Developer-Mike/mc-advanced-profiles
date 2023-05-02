import customtkinter as ctk
import tkinter as tk

class ThemedButton(ctk.CTkButton):
    def __init__(self, root, font_size = 15, primary = False, bold = False, **kwargs):
        if not primary:
            kwargs["fg_color"] = "black"
            kwargs["text_color"] = "white"

        kwargs["font"] = ("SeogeUI", font_size, "bold" if bold else "normal")

        super().__init__(root, **kwargs)

class ThemedEntry(ctk.CTkEntry):
    def __init__(self, root, font_size = 15, bold = False, enabled = True, **kwargs):
        kwargs["font"] = ("SeogeUI", font_size, "bold" if bold else "normal")

        super().__init__(root, **kwargs)

        self.set_enabled(enabled)

    def set_enabled(self, enabled: bool):
        self.configure(state=tk.NORMAL if enabled else tk.DISABLED)
        self.configure(text_color="white" if enabled else "gray")

    def insert(self, index, string):
        is_disabled = self.cget("state") == tk.DISABLED
        if is_disabled: self.configure(state=tk.NORMAL)

        super().insert(index, string)

        if is_disabled: self.configure(state=tk.DISABLED)