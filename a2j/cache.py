"""
aoe2record-to-json cache functions.
"""
import json
import os
from pathlib import Path

from a2j.encoder import JSONEncoder


def put(record: str, commands: list, data: dict):
    """
    Put JSON object in cache.

    :param (str) record: User-supplied record file.
    :param (list) commands: User-supplied commands.
    :param (dict) data: JSON object.
    """
    cache_file = file_path(record, commands)
    path = ""

    # CREATE MISSING DIRECTORIES
    for directory in cache_file.split("/")[:-1]:
        path += "/" + directory
        if not os.path.exists(path):
            os.mkdir(path)

    # DUMP JSON OBJECT INTO FILE
    with open(cache_file, "w") as file:
        json.dump(data, file, cls=JSONEncoder)
        file.close()


def get(record: str, commands: list) -> (dict, bool):
    """
    Get JSON object from cache.

    :param (str) record: User-supplied record file.
    :param (list) commands: User-supplied commands.
    :return: JSON object, True if cache file exists; otherwise False.
    :rtype: (dict, bool)
    """
    cache = {}
    cached = False
    cache_file = file_path(record, commands)

    if os.path.exists(cache_file):
        # IS CACHED
        cached = True

        # LOAD JSON OBJECT FROM FILE
        with open(cache_file, "r") as file:
            cache = json.load(file)
            file.close()

    return cache, cached


def file_path(record: str, commands: list) -> str:
    """
    Get path to cache file with data.

    :param (str) record: User-supplied record file.
    :param (list) commands: User-supplied commands.
    :return: File path.
    :rtype: str
    """
    commands.sort()

    return os.getcwd() + "/cache/" + ("/".join(commands)) + "/" + record


def clean(record: str) -> int:
    """
    Clean up all cached data related to record.

    :param (str) record: User-supplied record file.
    :return: True if successfully cleaned; otherwise False.
    :rtype: int
    """
    counter = 0

    for file in Path(os.getcwd() + "/cache").rglob(record):
        os.remove(file)
        counter += 1

    return counter
