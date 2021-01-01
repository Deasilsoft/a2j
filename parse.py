import json
import sys

from mgz.summary import Summary
from util.filename import filename


def commands():
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
        "restored": Summary.get_restored,
        "version": Summary.get_version,

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


def print_arguments():
    print("Arguments", end=": ")
    print("<file>", end=" ")
    print("<command>", end="\n")


def print_commands():
    print("Commands", end=": ")
    for key in commands().keys():
        if key != list(commands().keys())[-1]:
            print(key, end=", ")
        else:
            print(key, end=".\n")


if len(sys.argv) == 3:
    if filename(sys.argv[1]):
        with open("recs/" + sys.argv[1], "rb") as file:
            if sys.argv[2] in commands():
                summary = Summary(file)
                data = commands().get(sys.argv[2])(summary)
                # TODO: handle special commands (header, version...)
                print(json.dumps(data))
            else:
                print("[ERROR 2] ILLEGAL COMMAND")
                print_commands()
    else:
        print("[ERROR 3] ILLEGAL FILENAME")
else:
    print("[ERROR 1] ILLEGAL ARGUMENTS")
    print_arguments()
    print_commands()
