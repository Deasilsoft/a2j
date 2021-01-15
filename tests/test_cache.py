"""
Testing aoe2record-to-json caching.
"""

import json
import subprocess

PARSED = {}


def clean():
    """
    Initialize testing environment.
    """
    global PARSED

    cls = [
        "curl",
        "http://localhost:8080/a2j/v1/clean/?record=test.mgz"
    ]

    out, err = subprocess.Popen(cls, stdout=subprocess.PIPE).communicate()
    data = ""

    for line in out.splitlines():
        data += line.decode("utf-8")

    PARSED = json.loads(data)


def test_clean():
    clean()
    assert PARSED["success"] is True
    assert PARSED["cleaned"] is 1


def test_clean_empty():
    clean()
    assert PARSED["success"] is True
    assert PARSED["cleaned"] is 0
