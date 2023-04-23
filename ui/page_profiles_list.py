import tkinter as tk
import customtkinter as ctk
from ui.components.image_button import ImageButton
from utils.assets import PLUS_ICON_WHITE

class PageProfilesList(ctk.CTkFrame):
    def __init__(self, app):
        super().__init__(app)
        self.app = app

        ctk.CTkLabel(self, text="Profiles List").pack()

        bt_create_profile = ImageButton(self, PLUS_ICON_WHITE, size=(75, 75), padding=(30, 30), command=self._create_profile)
        bt_create_profile.pack(side=tk.BOTTOM, anchor="se", padx=40, pady=40)

    def _create_profile(self):
        self.app.navigate(self.app.pages[1])

    def update(self) -> None:
        # TODO: Update the profiles list

        return super().update()