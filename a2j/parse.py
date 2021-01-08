import json

import mgz.summary

from a2j.commands import get_commands
from a2j.encoder import JSONEncoder


def parse(record, commands):
    data = {
        "errors": []
    }

    try:
        with open(record, "rb") as file:
            perform = False

            for command in commands:
                if command in get_commands():
                    perform = True

                else:
                    data["errors"].append({
                        "message": "Command does not exist: " + command,
                        "errno": 1
                    })

            if perform:
                summary = None

                try:
                    mgz.summary.LOGGER.setLevel(9001)
                    summary = mgz.summary.Summary(file)

                except Exception as e:
                    data["errors"].append({
                        "message": "Parsing AoE2 record stopped with this error: " + str(e),
                        "errno": 2
                    })

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

    return json.dumps(data, indent=4, cls=JSONEncoder)
