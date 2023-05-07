import customtkinter as ctk
import tkinter as tk

from ui.components.themed_components import ThemedLabel

from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from ui.app import App
    from utils.mod import Mod

class ModSelection(ctk.CTkFrame):
    def __init__(self, root: any, app: "App", mods: List["Mod"], **kwargs):
        kwargs["fg_color"] = "transparent"
        super().__init__(root, **kwargs)

        lb_mods = ThemedLabel(self, text="Mods", font_size=30, bold=True)
        lb_mods.grid(row=0, column=0, sticky="w")