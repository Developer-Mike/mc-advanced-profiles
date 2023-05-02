import customtkinter as ctk
from PIL import Image, ImageDraw
from typing import Tuple

class ImageView(ctk.CTkLabel):
    def __init__(self, root, image: Image, size: Tuple[int] = None, radius: int = 0):
        super().__init__(root, text="")

        self.size = size
        self.radius = radius

        self._pil_image = None
        if image is not None:
            self.set_image(image)

    def set_image(self, image: Image):
        self._pil_image = image.copy()
        image = image.resize(self.size, Image.ANTIALIAS)

        if self.radius > 0:
            mask = Image.new("L", self.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.rounded_rectangle((0, 0) + self.size, self.radius, fill=255)

            image = image.copy().convert("RGB")
            image.putalpha(mask)

        ctk_image = ctk.CTkImage(image, size=self.size)
        self.configure(image=ctk_image)

    def get_image(self) -> Image:
        return self._pil_image