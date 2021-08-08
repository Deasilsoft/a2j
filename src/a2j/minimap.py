"""
https://github.com/Deasilsoft/a2j

Copyright (c),
2020-2021 Deasilsoft

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import PIL
from PIL import Image

from . import parse


def create(record: str, scale: int) -> Image:
    """
    Create the minimap image from record.

    :param (str) record: User-supplied record file.
    :param (int) scale: User-supplied scale.
    :return: Minimap image.
    :rtype: Image
    """

    # GET DATA FROM RECORD
    data = parse(record, ["map", "objects"])

    # DIMENSIONS OF MAP
    dimension = data["map"]["dimension"]

    # CREATE IMAGE OBJECT
    img = Image.new("RGB", (dimension, dimension))

    # DRAW TILES
    for tile in data["map"]["tiles"]:
        # GET VALUES FROM TILE
        tx, ty, tid, height = tile["x"], tile["y"], tile["terrain_id"], tile["elevation"]

        # DRAW ON IMAGE OBJECT
        img.putpixel((tx, ty), colors_terrain()[tid][0 if height < 3 else 1 if height < 5 else 2])

    # DRAW OBJECTS
    for obj in data["objects"]["objects"]:
        # GET VALUES FROM OBJECT
        ox, oy, oid, pid = int(obj["x"]), int(obj["y"]), obj["object_id"], obj["player_number"]

        # OBJECT OWNED BY PLAYER
        if pid is not None:
            img.putpixel((ox, oy), colors_players()[pid])

        # OTHER OBJECTS
        elif oid in colors_objects():
            img.putpixel((ox, oy), colors_objects()[oid])

    # UPSCALE IMAGE
    img = img.resize((min(max(scale, 1), 15) * dimension, min(max(scale, 1), 15) * dimension), PIL.Image.NEAREST)

    return img


def colors_objects() -> dict:
    """
    Age of Empires II object colors for minimap.

    Credit for a list of objects goes to:
        https://github.com/happyleavesaoc/aoc-mgz.

    :rtype: dict
    """

    food = (150, 200, 150)

    return {

        # FOOD
        48: food,  # BOAR
        59: food,  # BERRY BUSH
        65: food,  # DEER
        69: food,  # SHORE FISH
        450: food,  # MARLIN 1
        451: food,  # MARLIN 2
        452: food,  # DOLPHIN
        455: food,  # FISH 1
        456: food,  # FISH 2
        457: food,  # FISH 3
        458: food,  # FISH 4
        594: food,  # SHEEP
        810: food,  # IRON BOAR
        822: food,  # JAVELINA
        833: food,  # TURKEY
        1026: food,  # OSTRICH
        1031: food,  # CROCODILE
        1139: food,  # RHINOCEROS

        # GOLD
        66: (255, 215, 0),

        # STONE
        102: (145, 142, 133),

        # RELIC
        285: (255, 255, 255),

    }


def colors_players() -> dict:
    """
    Age of Empires II player colors for minimap.

    Credit for a list of Age of Empires II terrain and player colors goes to:
        https://github.com/goto-bus-stop/recanalyst.

    :rtype: dict
    """

    return {

        # BLUE
        0: (0, 0, 255),

        # RED
        1: (255, 0, 0),

        # GREEN
        2: (0, 255, 0),

        # YELLOW
        3: (255, 255, 0),

        # CYAN
        4: (0, 255, 255),

        # PINK
        5: (255, 0, 255),

        # GRAY
        6: (67, 67, 67),

        # ORANGE
        7: (255, 130, 1),

        # BLACK
        8: (0, 0, 0),

        # BLACK
        9: (0, 0, 0),

        # BLACK
        10: (0, 0, 0),

        # BLUE
        11: (0, 0, 255),

        # YELLOW
        12: (255, 255, 0),

        # WHITE
        13: (255, 255, 255),

        # RED
        14: (255, 0, 0),

    }


def colors_terrain() -> dict:
    """
    Age of Empires II terrain colors for minimap.

    Credit for a list of Age of Empires II terrain and player colors goes to:
        https://github.com/goto-bus-stop/recanalyst.

    This function has great potential for contributions from designers
    and other specialists.

    Got information what Terrain IDs are what?
    Got better color suggestions?

    Please create an issue https://github.com/Deasilsoft/a2j/issues!
    Pull requests would be even more awesome!

    :rtype: dict
    """

    return {

        0: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        # WATER
        1: {
            0: (48, 93, 182),
            1: (48, 93, 182),
            2: (48, 93, 182),
        },

        # SHORES
        2: {
            0: (248, 201, 138),
            1: (232, 180, 120),
            2: (189, 150, 111),
        },

        3: {
            0: (243, 170, 92),
            1: (228, 162, 82),
            2: (218, 156, 105),
        },

        4: {
            0: (84, 146, 176),
            1: (84, 146, 176),
            2: (84, 146, 176),
        },

        5: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        6: {
            0: (243, 170, 92),
            1: (228, 162, 82),
            2: (218, 156, 105),
        },

        7: {
            0: (138, 139, 87),
            1: (130, 136, 77),
            2: (118, 130, 65),
        },

        8: {
            0: (138, 139, 87),
            1: (130, 136, 77),
            2: (118, 130, 65),
        },

        9: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        10: {
            0: (37, 116, 57),
            1: (21, 118, 21),
            2: (0, 114, 0),
        },

        11: {
            0: (243, 170, 92),
            1: (228, 162, 82),
            2: (218, 156, 105),
        },

        12: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        # FOREST
        13: {
            0: (37, 116, 57),
            1: (21, 118, 21),
            2: (0, 114, 0),
        },

        14: {
            0: (248, 201, 138),
            1: (232, 180, 120),
            2: (189, 150, 111),
        },

        15: {
            0: (48, 93, 182),
            1: (48, 93, 182),
            2: (48, 93, 182),
        },

        # CLIFFS
        16: {
            0: (128, 100, 100),
            1: (128, 100, 100),
            2: (128, 100, 100),
        },

        17: {
            0: (37, 116, 57),
            1: (21, 118, 21),
            2: (0, 114, 0),
        },

        18: {
            0: (37, 116, 57),
            1: (21, 118, 21),
            2: (0, 114, 0),
        },

        19: {
            0: (37, 116, 57),
            1: (21, 118, 21),
            2: (0, 114, 0),
        },

        20: {
            0: (37, 116, 57),
            1: (21, 118, 21),
            2: (0, 114, 0),
        },

        21: {
            0: (37, 116, 57),
            1: (21, 118, 21),
            2: (0, 114, 0),
        },

        22: {
            0: (0, 74, 161),
            1: (0, 74, 161),
            2: (0, 74, 161),
        },

        23: {
            0: (0, 74, 187),
            1: (0, 74, 187),
            2: (0, 74, 187),
        },

        24: {
            0: (243, 170, 92),
            1: (228, 162, 82),
            2: (218, 156, 105),
        },

        25: {
            0: (243, 170, 92),
            1: (228, 162, 82),
            2: (218, 156, 105),
        },

        26: {
            0: (152, 192, 240),
            1: (152, 192, 240),
            2: (152, 192, 240),
        },

        27: {
            0: (243, 170, 92),
            1: (228, 162, 82),
            2: (218, 156, 105),
        },

        28: {
            0: (48, 93, 182),
            1: (48, 93, 182),
            2: (48, 93, 182),
        },

        29: {
            0: (138, 139, 87),
            1: (130, 136, 77),
            2: (118, 130, 65),
        },

        30: {
            0: (138, 139, 87),
            1: (130, 136, 77),
            2: (118, 130, 65),
        },

        31: {
            0: (138, 139, 87),
            1: (130, 136, 77),
            2: (118, 130, 65),
        },

        32: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        33: {
            0: (243, 170, 92),
            1: (228, 162, 82),
            2: (218, 156, 105),
        },

        34: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        35: {
            0: (152, 192, 240),
            1: (152, 192, 240),
            2: (152, 192, 240),
        },

        36: {
            0: (243, 170, 92),
            1: (228, 162, 82),
            2: (218, 156, 105),
        },

        37: {
            0: (152, 192, 240),
            1: (152, 192, 240),
            2: (152, 192, 240),
        },

        38: {
            0: (243, 170, 92),
            1: (228, 162, 82),
            2: (218, 156, 105),
        },

        39: {
            0: (243, 170, 92),
            1: (228, 162, 82),
            2: (189, 209, 253),
        },

        40: {
            0: (243, 170, 92),
            1: (228, 162, 82),
            2: (218, 156, 105),
        },

        41: {
            0: (243, 170, 92),
            1: (228, 162, 82),
            2: (218, 156, 105),
        },

        42: {
            0: (243, 170, 92),
            1: (228, 162, 82),
            2: (218, 156, 105),
        },

        43: {
            0: (243, 170, 92),
            1: (228, 162, 82),
            2: (218, 156, 105),
        },

        44: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        45: {
            0: (248, 201, 138),
            1: (232, 180, 120),
            2: (189, 150, 111),
        },

        46: {
            0: (248, 201, 138),
            1: (232, 180, 120),
            2: (189, 150, 111),
        },

        47: {
            0: (28, 28, 28),
            1: (28, 28, 28),
            2: (28, 28, 28),
        },

        48: {
            0: (37, 116, 57),
            1: (21, 118, 21),
            2: (0, 114, 0),
        },

        49: {
            0: (37, 116, 57),
            1: (21, 118, 21),
            2: (0, 114, 0),
        },

        50: {
            0: (37, 116, 57),
            1: (21, 118, 21),
            2: (0, 114, 0),
        },

        51: {
            0: (248, 201, 138),
            1: (232, 180, 120),
            2: (189, 150, 111),
        },

        52: {
            0: (248, 201, 138),
            1: (232, 180, 120),
            2: (189, 150, 111),
        },

        53: {
            0: (248, 201, 138),
            1: (232, 180, 120),
            2: (189, 150, 111),
        },

        54: {
            0: (84, 146, 176),
            1: (84, 146, 176),
            2: (84, 146, 176),
        },

        55: {
            0: (37, 116, 57),
            1: (21, 118, 21),
            2: (0, 114, 0),
        },

        56: {
            0: (37, 116, 57),
            1: (21, 118, 21),
            2: (0, 114, 0),
        },

        57: {
            0: (0, 74, 161),
            1: (0, 74, 161),
            2: (0, 74, 161),
        },

        58: {
            0: (0, 84, 176),
            1: (0, 84, 176),
            2: (0, 84, 176),
        },

        59: {
            0: (84, 146, 176),
            1: (84, 146, 176),
            2: (84, 146, 176),
        },

        60: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        61: {
            0: (243, 170, 92),
            1: (228, 162, 82),
            2: (218, 156, 105),
        },

        62: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        63: {
            0: (138, 139, 87),
            1: (130, 136, 77),
            2: (118, 130, 65),
        },

        64: {
            0: (138, 139, 87),
            1: (130, 136, 77),
            2: (118, 130, 65),
        },

        65: {
            0: (138, 139, 87),
            1: (130, 136, 77),
            2: (118, 130, 65),
        },

        66: {
            0: (138, 139, 87),
            1: (130, 136, 77),
            2: (118, 130, 65),
        },

        67: {
            0: (138, 139, 87),
            1: (130, 136, 77),
            2: (118, 130, 65),
        },

        68: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        69: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        70: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        71: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        72: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        73: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        74: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        75: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        76: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        77: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        78: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        79: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        80: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        81: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        82: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        83: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        84: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        85: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        86: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        87: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        88: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        89: {
            0: (0, 169, 0),
            1: (51, 151, 39),
            2: (0, 141, 0),
        },

        90: {
            0: (84, 146, 176),
            1: (84, 146, 176),
            2: (84, 146, 176),
        },

        91: {
            0: (84, 146, 176),
            1: (84, 146, 176),
            2: (84, 146, 176),
        },

        92: {
            0: (84, 146, 176),
            1: (84, 146, 176),
            2: (84, 146, 176),
        },

        93: {
            0: (84, 146, 176),
            1: (84, 146, 176),
            2: (84, 146, 176),
        },

        94: {
            0: (84, 146, 176),
            1: (84, 146, 176),
            2: (84, 146, 176),
        },

        95: {
            0: (48, 93, 182),
            1: (48, 93, 182),
            2: (48, 93, 182),
        },

        96: {
            0: (48, 93, 182),
            1: (48, 93, 182),
            2: (48, 93, 182),
        },

        97: {
            0: (48, 93, 182),
            1: (48, 93, 182),
            2: (48, 93, 182),
        },

        98: {
            0: (48, 93, 182),
            1: (48, 93, 182),
            2: (48, 93, 182),
        },

        99: {
            0: (48, 93, 182),
            1: (48, 93, 182),
            2: (48, 93, 182),
        }

    }
