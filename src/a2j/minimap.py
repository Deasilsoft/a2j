"""
a2j minimap functions.
"""
from PIL import Image


def draw(size) -> Image:
    """
    Draw the minimap image.
    """
    return Image.new("RGB", (size, size))


def colors() -> dict:
    """
    Dictionary of colors.
    :return:
    """
    return dict()
