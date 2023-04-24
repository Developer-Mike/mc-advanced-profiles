import tkinter as tk
import customtkinter as ctk

class PageCreateProfile(ctk.CTkFrame):
    def __init__(self, app):
        super().__init__(app, fg_color="transparent")
        self.app = app

        ctk.CTkLabel(self, text="Create Profile").pack()
        ctk.CTkButton(self, text="Back", command=lambda: self.app.navigate(self.app.pages[0])).pack()