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

import re
import urllib.parse
from pathlib import Path
from typing import List

from .commands import match_commands, summary_commands


def validate_commands(command_list: List[str], method: str) -> bool:
    """
    Is the list of user-supplied commands valid?

    :param (List[str]) command_list: User-supplied commands.
    :param (str) method: User-supplied method.
    :return: bool
    """

    return not invalid_commands(command_list, method)


def validate_method(method: str) -> bool:
    """
    Is the user-supplied method valid?

    :param (str) method: User-supplied method.
    :return: bool
    """

    return method in ["summary", "match"]


def valid_summary_commands(command_list: List[str]) -> List[str]:
    """
    Get list of valid summary commands from list of commands.

    :param (list) command_list: User-supplied commands.
    :return:
    """

    return [command for command in command_list if command in summary_commands()]


def valid_match_commands(command_list: List[str]) -> List[str]:
    """
    Get list of valid match commands from list of commands.

    :param (list) command_list: User-supplied commands.
    :return:
    """

    return [command for command in command_list if command in match_commands()]


def invalid_commands(command_list: List[str], method: str) -> List[str]:
    """
    Get list of invalid commands from list of commands.

    :param (list) command_list: User-supplied commands.
    :param (str) method: User-supplied method.
    :return:
    """

    if not validate_method(method):
        raise ValueError("Invalid method supplied.")

    commands = {
        "summary": summary_commands,
        "match": match_commands,
    }

    return [command for command in command_list if command not in commands.get(method)()]


def is_record(path: str) -> bool:
    """
    Is filename a record file?

    :param (str) path: User-supplied filename.
    :return: True if filename is valid record file; otherwise False.
    :rtype: bool
    """

    return re.search(r"^\.+|\\|/", urllib.parse.unquote_plus(path)) is None and get_record(path).exists()


def get_record(path: str) -> Path:
    """
    Get record file path by filename.

    :param path: User-supplied filename.
    :return: User-supplied record file.
    :rtype: str
    """

    return Path.cwd() / "records" / path
