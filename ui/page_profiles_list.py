import tkinter as tk
import customtkinter as ctk

class PageProfilesList(ctk.CTkFrame):
    def __init__(self, app):
        super().__init__(app)
        self.app = app

        ctk.CTkLabel(self, text="Profiles List").pack()
        ctk.CTkButton(self, text="Create Profile", command=lambda: self.app.navigate(self.app.pages[1])).pack()