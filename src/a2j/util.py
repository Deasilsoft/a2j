"""
a2j utility functions.
"""
from pathlib import Path


def is_record(path: str) -> bool:
    """
    Is filename a record file?

    :param (str) path: User-supplied filename.
    :return: True if filename is valid record file; otherwise False.
    :rtype: bool
    """
    return path.find("..") == -1


def record(path: str) -> str:
    """
    Get record file path by filename.

    :param path: User-supplied filename.
    :return: User-supplied record file.
    :rtype: str
    """
    return Path(__file__).parent.parent.absolute() / "records" / path
