"""
a2j utility functions.
"""
import re
from pathlib import Path
from typing import List

from mgz.summary import Summary


def validate_commands(commands: list) -> bool:
    """
    Is the list of user-supplied commands valid?

    :param (list) commands: User-supplied commands.
    :return: bool
    """
    return not invalid_commands(commands)


def invalid_commands(commands: List[str]) -> List[str]:
    """
    Get list of invalid commands from list of commands.

    :param commands:
    :return:
    """
    return [command for command in commands if command not in get_commands().keys()]


def get_commands() -> dict:
    """
    :return: Object with available commands.
    :rtype: dict
    """
    return {
        # META
        "completed": Summary.get_completed,
        "dataset": Summary.get_dataset,
        "encoding": Summary.get_encoding,
        "file_hash": Summary.get_file_hash,
        "hash": Summary.get_hash,
        "language": Summary.get_language,
        "mirror": Summary.get_mirror,
        "owner": Summary.get_owner,
        "platform": Summary.get_platform,
        "restored": __get_restored,
        "version": __get_version,

        # PLAYERS
        "chat": Summary.get_chat,
        "diplomacy": Summary.get_diplomacy,
        "players": Summary.get_players,
        "profiles": Summary.get_profile_ids,
        "ratings": Summary.get_ratings,
        "teams": Summary.get_teams,
        "achievements": Summary.has_achievements,

        # GAME
        "duration": Summary.get_duration,
        "map": Summary.get_map,
        "objects": Summary.get_objects,
        "postgame": Summary.get_postgame,
        "settings": Summary.get_settings,
        "start_time": Summary.get_start_time,
    }


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
    return Path(__file__).parent.parent.parent.resolve() / "records" / path


def __get_restored(summary: Summary) -> dict:
    """
    :return: Objectified restored array from record.
    :rtype: dict
    """
    return {
        "is_restored": summary.get_restored()[0],
        "time": summary.get_restored()[1],
    }


def __get_version(summary: Summary) -> dict:
    """
    :return: Objectified version array from record.
    :rtype: dict
    """
    return {
        "recanalyst": summary.get_version()[0],
        "game": summary.get_version()[1],
        "save": summary.get_version()[2],
        "log": summary.get_version()[3],
    }
