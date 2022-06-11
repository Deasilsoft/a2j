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

from mgz.summary import Summary


def available_commands() -> dict:
    """
    :return: Dict with available commands.
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
        "achievements": Summary.has_achievements,
        "chat": Summary.get_chat,
        "diplomacy": Summary.get_diplomacy,
        "players": Summary.get_players,
        "profiles": Summary.get_profile_ids,
        "ratings": Summary.get_ratings,
        "teams": Summary.get_teams,

        # GAME
        "duration": Summary.get_duration,
        "map": Summary.get_map,
        "objects": Summary.get_objects,
        "postgame": Summary.get_postgame,
        "settings": Summary.get_settings,
        "start_time": Summary.get_start_time,
    }


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
