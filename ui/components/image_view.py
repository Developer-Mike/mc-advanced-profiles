import customtkinter as ctk
import tkinter as tk
from PIL import Image
from typing import Tuple

class ImageView(ctk.CTkLabel):
    def __init__(self, root, image: Image, size: Tuple[int] = None):
        super().__init__(root, text="", image=ctk.CTkImage(image, size=size))