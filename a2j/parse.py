import mgz.summary

import a2j.util
from a2j.commands import get_commands


def parse(record: str, commands: list) -> dict:
    data = {
        "errors": []
    }

    if a2j.util.is_record(record):
        try:
            with open(a2j.util.record(record), "rb") as file:
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

    else:
        data["errors"].append({
            "message": "Injection attempt detected: " + record,
            "errno": 100
        })

    return data
