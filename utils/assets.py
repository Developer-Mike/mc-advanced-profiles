import os
from PIL import Image, ImageOps

_ROOT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")

def invert(image):
    r, g, b, a = image.split()
    rgb_image = Image.merge('RGB', (r, g, b))

    inverted_image = ImageOps.invert(rgb_image)

    r2, g2, b2 = inverted_image.split()
    return Image.merge('RGBA', (r2, g2, b2, a))

PLUS_ICON_BLACK = Image.open(os.path.join(_ROOT_DIR, "plus.png")).convert("RGBA")
PLUS_ICON_WHITE = invert(PLUS_ICON_BLACK)

    