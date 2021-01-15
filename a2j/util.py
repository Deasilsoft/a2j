"""
aoe2record-to-json utility functions.
"""


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
    return "records/" + path
