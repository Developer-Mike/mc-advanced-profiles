import customtkinter as ctk
from PIL import Image
from typing import Tuple

class ImageButton(ctk.CTkButton):
    def __init__(self, master: any, image: Image, size: Tuple[int], padding: Tuple[int] = (0, 0), transparent = False, command = None):
        ctk_image = ctk.CTkImage(image, size=(size[0] - padding[0], size[1] - padding[1]))

        transparent_args = {}
        if transparent:
            transparent_args = {"fg_color": "transparent", "hover_color": "#3c3c3c"}
        
        super().__init__(master, text="", image=ctk_image, width=size[0], height=size[1], command=command, **transparent_args)