"""
a2j utility functions.
"""
import re
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
    return re.search(r"(\.{2,}|\\|/)", path) is None and get_record(path).exists()


def get_record(path: str) -> Path:
    """
    Get record file path by filename.

    :param path: User-supplied filename.
    :return: User-supplied record file.
    :rtype: str
    """
    return Path.cwd() / "records" / path
