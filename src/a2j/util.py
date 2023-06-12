"""
https://github.com/Deasilsoft/a2j

Copyright (c) 2020-2023 Deasilsoft

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
from os.path import commonpath, normpath, realpath
from pathlib import Path
from typing import List
from urllib.parse import unquote_plus

from .commands import get_match_commands, get_summary_commands
from .constant import METHODS, RECORD_DIRECTORY


def is_valid_command(command_list: List[str], method: str) -> bool:
    """
    Is the list of user-supplied commands valid?

    :param (List[str]) command_list: User-supplied commands.
    :param (str) method: User-supplied method.
    :return: bool
    """

    return not get_invalid_commands(command_list, method)


def is_valid_method(method: str) -> bool:
    """
    Is the user-supplied method valid?

    :param (str) method: User-supplied method.
    :return: bool
    """

    return method in METHODS


def get_valid_commands(command_list: List[str], method: str) -> List[str]:
    """
    Get list of valid summary commands from list of commands.

    :param (list) command_list: User-supplied commands.
    :param (str) method: User-supplied method.
    :return:
    """

    commands = {
        "summary": get_summary_commands,
        "match": get_match_commands,
    }

    return [command for command in command_list if command in commands.get(method)()]


def get_invalid_commands(command_list: List[str], method: str) -> List[str]:
    """
    Get list of invalid commands from list of commands.

    :param (list) command_list: User-supplied commands.
    :param (str) method: User-supplied method.
    :return:
    """

    commands = {
        "summary": get_summary_commands,
        "match": get_match_commands,
    }

    return [command for command in command_list if command not in commands.get(method)()]


def handle_record(filename: str) -> str:
    """
    Handle filename of record file.

    :param (str) filename: User-supplied filename.
    :return: Handles record filename.
    """

    # Handle special URL characters
    filename = unquote_plus(filename)

    # Handle path normalization
    filename = normpath(filename)

    return filename


def is_record(filename: str) -> bool:
    """
    Is filename a record file?

    :param (str) filename: User-supplied filename.
    :return: True if filename is valid record file; otherwise False.
    :rtype: bool
    """

    # Validate path
    if str(RECORD_DIRECTORY) != commonpath((str(RECORD_DIRECTORY), realpath(str(get_record_path(filename))))):
        return False

    # Validate file existence
    if not get_record_path(filename).exists():
        return False

    return True


def get_record_path(filename: str) -> Path:
    """
    Get record file path by filename.

    :param (str) filename: User-supplied filename.
    :return: User-supplied record file.
    :rtype: str
    """

    return RECORD_DIRECTORY / filename


def get_version() -> str:
    """
    Get the version of a2j.

    :return:  Version of a2j.
    :rtype: str
    """

    # OPEN VERSION FILE
    with open(Path.cwd() / "VERSION", "r") as file:
        # READ VERSION FROM FILE
        version = file.read().strip()

        # CLOSE FILE
        file.close()

    return version
