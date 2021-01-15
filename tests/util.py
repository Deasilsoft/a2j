"""
Testing util functions.
"""
import json

import subprocess


def execute(cls: list):
    """
    :param (list) cls: System commands to execute.
    :return: JSON Object.
    :rtype: dict
    """
    out, err = subprocess.Popen(cls, stdout=subprocess.PIPE).communicate()
    raw = ""

    for line in out.splitlines():
        raw += line.decode("utf-8")

    return json.loads(raw)
