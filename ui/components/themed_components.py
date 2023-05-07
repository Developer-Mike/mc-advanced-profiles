import customtkinter as ctk
import tkinter as tk

class ThemedButton(ctk.CTkButton):
    def __init__(self, root, font_size = 15, primary = False, bold = False, **kwargs):
        if not primary:
            kwargs["fg_color"] = "black"
            kwargs["text_color"] = "white"

        kwargs["font"] = ("SeogeUI", font_size, "bold" if bold else "normal")

        super().__init__(root, **kwargs)

class ThemedLabel(ctk.CTkLabel):
    def __init__(self, root, font_size = 15, bold = False, **kwargs):
        kwargs["font"] = ("SeogeUI", font_size, "bold" if bold else "normal")
        super().__init__(root, **kwargs)

class ThemedEntry(ctk.CTkFrame):
    def __init__(self, root, label=None, font_size = 15, bold = False, enabled = True, **kwargs):
        kwargs["font"] = ("SeogeUI", font_size, "bold" if bold else "normal")

        super().__init__(root, fg_color="transparent")

        if label is not None: 
            self.label = ThemedLabel(self, text=label, font_size=font_size, bold=bold)
            self.label.pack(side=tk.RIGHT, padx=(10, 0))

        self.entry = ctk.CTkEntry(self, **kwargs)
        self.entry.pack(side=tk.LEFT)

        self.set_enabled(enabled)

    def set_enabled(self, enabled: bool):
        self.entry.configure(state=tk.NORMAL if enabled else tk.DISABLED)
        self.entry.configure(text_color="white" if enabled else "gray")

    def insert(self, index, string):
        is_disabled = self.entry.cget("state") == tk.DISABLED
        if is_disabled: self.entry.configure(state=tk.NORMAL)

        self.entry.insert(index, string)

        if is_disabled: self.entry.configure(state=tk.DISABLED)


class ThemedDropdown(ctk.CTkComboBox):
    def __init__(self, root, font_size = 15, bold = False, **kwargs):
        kwargs["state"] = "readonly"
        kwargs["font"] = ("SeogeUI", font_size, "bold" if bold else "normal")

        super().__init__(root, **kwargs)