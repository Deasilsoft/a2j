"""
Testing util functions.
"""
import json

import subprocess
from json.decoder import JSONDecodeError


def fetch(cls: list):
    """
    :param (list) cls: System commands to execute.
    :return: JSON Object.
    :rtype: dict
    """
    # RUN PROCESS
    out, err = subprocess.Popen(cls, stdout=subprocess.PIPE).communicate()

    # HANDLE ERROR
    if err is not None:
        return None, err

    # RAW DATA
    raw = ""

    # READ RAW DATA
    for line in out.splitlines():
        raw += line.decode("utf-8")

    # PARSE JSON
    try:
        data = json.loads(raw)

    # HANDLE JSON ERROR
    except JSONDecodeError as err:
        return None, err

    # RETURN PARSED JSON
    return data, None
