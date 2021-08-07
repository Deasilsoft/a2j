"""
https://github.com/Deasilsoft/a2j

Copyright (c) 2020-2021 Deasilsoft

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

from pathlib import Path
from typing import List

from .commands import available_commands


def validate_commands(commands: list) -> bool:
    """
    Is the list of user-supplied commands valid?

    :param (list) commands: User-supplied commands.
    :return: bool
    """

    return not invalid_commands(commands)


def valid_commands(commands: List[str]) -> List[str]:
    """
    Get list of valid commands from list of commands.

    :param (list) commands: User-supplied commands.
    :return:
    """

    return [command for command in commands if command in available_commands()]


def invalid_commands(commands: List[str]) -> List[str]:
    """
    Get list of invalid commands from list of commands.

    :param (list) commands: User-supplied commands.
    :return:
    """

    return [command for command in commands if command not in available_commands()]


def is_record(path: str) -> bool:
    """
    Is filename a record file?

    :param (str) path: User-supplied filename.
    :return: True if filename is valid record file; otherwise False.
    :rtype: bool
    """

    return path != "" and ".." not in path and "/" not in path and "\\" not in path and get_record(path).exists()


def get_record(path: str) -> Path:
    """
    Get record file path by filename.

    :param path: User-supplied filename.
    :return: User-supplied record file.
    :rtype: str
    """

    return Path.cwd() / "records" / path
