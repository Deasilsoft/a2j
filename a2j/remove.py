import os
import logging

from a2j.util import is_record, get_record


def remove(arguments):
    path = arguments[2]

    if is_record(path):
        record = get_record(path)

        if os.path.exists(record):
            logging.info("Removing file: " + record)
            os.remove(record)
            logging.info("File removed.")

        else:
            logging.warning("File not found: " + record)

    else:
        logging.error("Path is not to a valid record location.")
