"""
a2j CRUD-cache functions.
"""
import json
import os
from pathlib import Path

from . import encoder


def create(record: str, commands: list, data: dict):
    """
    Put JSON object in cache.

    :param (str) record: User-supplied record file.
    :param (list) commands: User-supplied commands.
    :param (dict) data: JSON object.
    """
    cache_file = get_path(record, commands)
    path = ""

    # CREATE MISSING DIRECTORIES
    for directory in cache_file.split(os.sep)[:-1]:
        path += os.sep + directory
        if not os.path.exists(path):
            os.mkdir(path)

    # DUMP JSON OBJECT INTO FILE
    with open(cache_file, "w") as file:
        json.dump(data, file, cls=encoder.JSONEncoder)
        file.close()


def read(record: str, commands: list) -> (dict, bool):
    """
    Get JSON object from cache.

    :param (str) record: User-supplied record file.
    :param (list) commands: User-supplied commands.
    :return: JSON object, True if cache file exists; otherwise False.
    :rtype: (dict, bool)
    """
    cached_data = {}
    is_cached = False
    cache_file = get_path(record, commands)

    if os.path.exists(cache_file):
        # IS CACHED
        is_cached = True

        # LOAD JSON OBJECT FROM FILE
        with open(cache_file, "r") as file:
            cached_data = json.load(file)
            file.close()

    return cached_data, is_cached


def delete(record: str) -> int:
    """
    Clean up all cached data related to record.

    :param (str) record: User-supplied record file.
    :return: True if successfully cleaned; otherwise False.
    :rtype: int
    """
    counter = 0

    for file in Path(Path(__file__).parent.parent.absolute() / "cache").rglob(record):
        os.remove(file)
        counter += 1

    return counter


def get_path(record: str, commands: list) -> str:
    """
    Get path to cache file with data.

    :param (str) record: User-supplied record file.
    :param (list) commands: User-supplied commands.
    :return: File path.
    :rtype: str
    """
    commands.sort()

    print(Path(__file__).parent.parent.absolute() / "cache" / (os.sep.join(commands)) / record)

    return Path(__file__).parent.parent.absolute() / "cache" / (os.sep.join(commands)) / record
