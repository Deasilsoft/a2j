import json
import sys

from mgz.summary import Summary
from util.record import is_record, record


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


if len(sys.argv) > 2:
    if is_record(sys.argv[1]):
        with open(record(sys.argv[1]), "rb") as file:
            del sys.argv[0], sys.argv[0]
            perform = False

            for command in sys.argv:
                if command in commands():
                    perform = True
                else:
                    print("[WARNING] UNKNOWN COMMAND", end=": ")
                    print(command)

            if perform:
                summary = Summary(file)
                output = {}

                for command in sys.argv:
                    if command in commands():
                        data = commands().get(command)(summary)
                        # TODO: handle special commands (header, version...)
                        output[command] = data

                print(json.dumps(output))
            else:
                print("[ERROR 2] ILLEGAL COMMANDS")
                print_commands()

            file.close()
    else:
        print("[ERROR 3] ILLEGAL FILENAME")
else:
    print("[ERROR 1] ILLEGAL ARGUMENTS")
    print_arguments()
    print_commands()
