import customtkinter as ctk
from PIL import Image, ImageDraw, ImageOps
from typing import Tuple

class ImageView(ctk.CTkLabel):
    def __init__(self, root, image: Image, size: Tuple[int] = None, radius: int = 0):
        if radius > 0:
            mask = Image.new("L", image.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.rounded_rectangle((0, 0) + image.size, radius, fill=255)

            image = image.copy().convert("RGB")
            image.putalpha(mask)

        ctk_image = ctk.CTkImage(image, size=size)
        super().__init__(root, text="", image=ctk_image)