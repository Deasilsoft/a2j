import os
import logging

from a2j.util import is_record, get_record


def append(arguments):
    path = arguments[2]
    content = arguments[3]

    if is_record(path):
        record = get_record(path)

        if not os.path.exists(record):
            logging.info("Creating file: " + record)

            try:
                with open(record, "w") as file:
                    file.write(content)
                    file.close()
                    logging.info("File created with content.")

            except FileNotFoundError as e:
                logging.error("Record does not exist: " + e.filename)

        else:
            logging.info("Opening file: " + record)

            try:
                with open(record, "a") as file:
                    file.write(content)
                    file.close()
                    logging.info("Content appended to file.")

            except FileNotFoundError as e:
                logging.error("Record does not exist: " + e.filename)

    else:
        logging.error("Path is not to a valid record location.")
