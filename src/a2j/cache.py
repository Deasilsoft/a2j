"""
https://github.com/Deasilsoft/a2j

Copyright (c) 2020-2022 Deasilsoft

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

import json
from pathlib import Path

from .constant import CACHE_DIRECTORY
from .encoder import JSONEncoder


def create_cache(record: str, commands: list, method: str, data: dict):
    """
    Put JSON object in cache.

    :param (str) record: User-supplied record file.
    :param (list) commands: User-supplied commands.
    :param (str) method: User-supplied method.
    :param (dict) data: JSON object.
    """

    cache_file = get_cache_path(record, commands, method)

    # CREATE MISSING DIRECTORIES
    cache_file.parent.mkdir(parents=True, exist_ok=True)

    # DUMP JSON OBJECT INTO FILE
    with cache_file.open(mode="w") as file:
        json.dump(data, file, cls=JSONEncoder)
        file.close()


def read_cache(record: str, commands: list, method: str) -> (dict, bool):
    """
    Get JSON object from cache.

    :param (str) record: User-supplied record file.
    :param (list) commands: User-supplied commands.
    :param (str) method: User-supplied method.
    :return: JSON object, True if cache file exists; otherwise False.
    :rtype: (dict, bool)
    """

    cached_data = {}
    is_cached = False
    cache_file = get_cache_path(record, commands, method)

    if cache_file.exists():
        # IS CACHED
        is_cached = True

        # LOAD JSON OBJECT FROM FILE
        with cache_file.open() as file:
            cached_data = json.load(file)
            file.close()

    return cached_data, is_cached


def delete_cache(record: str) -> int:
    """
    Clean up all cached data related to record.

    :param (str) record: User-supplied record file.
    :return: True if successfully cleaned; otherwise False.
    :rtype: int
    """

    counter = 0

    for file in CACHE_DIRECTORY.rglob(record):
        file.unlink()
        counter += 1

    return counter


def get_cache_path(record: str, commands: list, method: str) -> Path:
    """
    Get path to cache file with data.

    :param (str) record: User-supplied record file.
    :param (list) commands: User-supplied commands.
    :param (str) method: User-supplied method.
    :return: File path.
    :rtype: str
    """

    commands.sort()

    return CACHE_DIRECTORY.joinpath(method).joinpath(*commands) / record
