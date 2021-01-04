import json
import logging

from mgz.summary import Summary
from a2j.util import is_record, get_record
from a2j.commands import get_commands
from a2j.encoder import JSONEncoder


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
                            output[command] = get_commands().get(command)(summary)

                    print(json.dumps(output, indent=4, cls=JSONEncoder))

                file.close()

        except FileNotFoundError as e:
            logging.error("Record does not exist: " + e.filename)

    else:
        logging.error("Path is not to a valid record location.")
