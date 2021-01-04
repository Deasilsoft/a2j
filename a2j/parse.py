import json
import logging

from mgz.summary import Summary
from a2j.util import is_record, get_record
from a2j.commands import get_commands


def parse(arguments):
    path = arguments[2]
    commands = arguments[3:]

    if is_record(path):
        record = get_record(path)

        try:
            with open(record, "rb") as file:
                perform = False

                for command in commands:
                    if command in get_commands():
                        perform = True
                    else:
                        logging.warning("Invalid command: " + command)

                if perform:
                    summary = Summary(file)
                    output = {}

                    for command in commands:
                        if command in get_commands():
                            data = get_commands().get(command)(summary)
                            # TODO: handle special commands (header, version...)
                            output[command] = data

                    print(json.dumps(output))

                file.close()

        except FileNotFoundError as e:
            logging.error("Record does not exist: " + e.filename)

    else:
        logging.error("Path is not to a valid record location.")
