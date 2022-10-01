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
from typing import Dict, List

from mgz.summary import FullSummary


def get_match_commands() -> List[str]:
    """
    :return: List with available match commands.
    :rtype: List[str]
    """

    return [
        # SPECIAL
        "all",

        # META
        "completed",
        "diplomacy_type",
        "file",
        "game_version",
        "guid",
        "hash",
        "log_version",
        "multiqueue",
        "save_version",
        "version",

        # PLAYERS
        "chat",
        "players",
        "teams",

        # SETTINGS
        "all_technologies",
        "cheats",
        "dataset",
        "difficulty",
        "difficulty_id",
        "lock_speed",
        "lock_teams",
        "map_reveal",
        "map_reveal_id",
        "population",
        "speed",
        "speed_id",
        "starting_age",
        "starting_age_id",
        "team_together",
        "type",
        "type_id",

        # GAME
        "actions",
        "duration",
        "gaia",
        "inputs",
        "lobby",
        "map",
    ]


def get_summary_commands() -> Dict[str, callable]:
    """
    :return: Dict with available summary commands.
    :rtype: dict
    """

    return {
        # SPECIAL
        "all": None,

        # META
        "completed": FullSummary.get_completed,
        "dataset": FullSummary.get_dataset,
        "encoding": FullSummary.get_encoding,
        "file_hash": FullSummary.get_file_hash,
        "hash": FullSummary.get_hash,
        "language": FullSummary.get_language,
        "mirror": FullSummary.get_mirror,
        "owner": FullSummary.get_owner,
        "platform": FullSummary.get_platform,
        "restored": __get_restored,
        "version": __get_version,

        # PLAYERS
        "achievements": FullSummary.has_achievements,
        "chat": FullSummary.get_chat,
        "diplomacy": FullSummary.get_diplomacy,
        "players": FullSummary.get_players,
        "profiles": FullSummary.get_profile_ids,
        "ratings": FullSummary.get_ratings,
        "teams": FullSummary.get_teams,

        # GAME
        "duration": FullSummary.get_duration,
        "map": FullSummary.get_map,
        "objects": FullSummary.get_objects,
        "postgame": FullSummary.get_postgame,
        "settings": FullSummary.get_settings,
        "start_time": FullSummary.get_start_time,
    }


def __get_restored(summary: FullSummary) -> Dict[str, any]:
    """
    :return: Objectified restored array from record.
    :rtype: dict
    """

    is_restored, restore_time = summary.get_restored()

    return {
        "is_restored": is_restored,
        "time": restore_time,
    }


def __get_version(summary: FullSummary) -> Dict[str, any]:
    """
    :return: Objectified version array from record.
    :rtype: dict
    """

    recanalyst_version, game_version, save_version, log_version, build = summary.get_version()

    return {
        "recanalyst": recanalyst_version,
        "game": game_version,
        "save": save_version,
        "log": log_version,
        "build": build,
    }
