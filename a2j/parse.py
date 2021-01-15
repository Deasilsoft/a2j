"""
aoe2record-to-json parsing functions.
"""
import mgz.summary

import a2j.cache
import a2j.util
from a2j.commands import get_commands


def parse(record: str, commands: list) -> dict:
    """
    Parse Age of Empires II record and retrieve JSON object built on the user-supplied commands.

    :param (str) record: User-supplied record file.
    :param (list) commands: User-supplied commands.
    :return: JSON object
    :rtype: dict
    """
    data = {
        "errors": []
    }

    # SORT COMMANDS TO HAVE A REPEATABLE STRUCTURE OF THE JSON OBJECT
    commands.sort()

    # CHECK IF USER-INPUT IS VALID; THEN OPEN THE RECORD FILE
    if a2j.util.is_record(record):

        # FIRST GET CACHE IF AVAILABLE
        cache, cached = a2j.cache.get(record, commands)

        if cached:
            data = cache

        else:
            try:
                with open(a2j.util.record(record), "rb") as file:
                    perform = False

                    # CHECK IF ANY COMMAND IS VALID; TO PREVENT PARSING THE RECORD WITH NO OUTPUT
                    for command in commands:
                        if command in get_commands():
                            perform = True

                        else:
                            data["errors"].append({
                                "message": "Command does not exist: " + command,
                                "errno": 1
                            })

                    # GO AHEAD AND PERFORM THE RECORD PARSING
                    if perform:
                        summary = None

                        try:
                            # SET THE LOGGER TO AN IMPOSSIBLY HIGH LEVEL TO PREVENT WEIRD OUTPUT
                            mgz.summary.LOGGER.setLevel(9001)
                            summary = mgz.summary.Summary(file)

                        except Exception as e:
                            data["errors"].append({
                                "message": "Parsing AoE2 record stopped with this error: " + str(e),
                                "errno": 2
                            })

                        # PUT THE RECORD DATA INSIDE OUR ARRAY
                        if summary is not None:
                            for command in commands:
                                if command in get_commands():
                                    data[command] = get_commands().get(command)(summary)

                    file.close()

            except FileNotFoundError as e:
                data["errors"].append({
                    "message": "Record does not exist: " + e.filename,
                    "errno": 0
                })

            # PUT TO CACHE
            a2j.cache.put(record, commands, data)

    else:
        data["errors"].append({
            "message": "Injection attempt detected: " + record,
            "errno": 100
        })

    return data
