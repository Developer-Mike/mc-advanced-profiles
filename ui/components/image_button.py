import customtkinter as ctk
from PIL import Image
from typing import Tuple

class ImageButton(ctk.CTkButton):
    def __init__(self, master: any, image: Image, size: Tuple[int], padding: Tuple[int] = (0, 0), command = None):
        ctk_image = ctk.CTkImage(image, size=(size[0] - padding[0], size[1] - padding[1]))
        super().__init__(master, text="", image=ctk_image, width=size[0], height=size[1], command=command)