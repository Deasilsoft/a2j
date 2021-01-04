import json
import logging

import mgz.summary

from a2j.commands import get_commands
from a2j.encoder import JSONEncoder


def parse(arguments):
    path = arguments[2]
    commands = arguments[3:]

    try:
        with open(path, "rb") as file:
            perform = False

            for command in commands:
                if command in get_commands():
                    perform = True
                else:
                    logging.warning("Invalid command: " + command)

            if perform:
                mgz.summary.LOGGER.setLevel(logging.ERROR)
                summary = mgz.summary.Summary(file)
                objects = {}

                for command in commands:
                    if command in get_commands():
                        objects[command] = get_commands().get(command)(summary)

                print(json.dumps(objects, indent=4, cls=JSONEncoder))

            file.close()

    except FileNotFoundError as e:
        logging.error("Record does not exist: " + e.filename)
