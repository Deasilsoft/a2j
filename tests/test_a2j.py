"""
Testing aoe2record-to-json core functionality.
"""
import json
import subprocess

from a2j.commands import get_commands

PARSED = {}
READ = {}
INITIALIZED = False


def initialize():
    """
    Initialize testing environment.
    """
    global PARSED, READ, INITIALIZED

    if INITIALIZED is False:
        cls = [
            "curl",
            "http://localhost:8080/a2j/v1/parse/" + "/".join(get_commands().keys()) + "/?record=test.mgz"
        ]

        out, err = subprocess.Popen(cls, stdout=subprocess.PIPE).communicate()
        data = ""

        for line in out.splitlines():
            data += line.decode("utf-8")

        PARSED = json.loads(data)

        with open("tests/data/test.json", "r") as file:
            READ = json.loads(file.read())
            file.close()

        INITIALIZED = True


def test_completed():
    initialize()
    assert PARSED["completed"] == READ["completed"]


def test_dataset():
    initialize()
    assert PARSED["dataset"] == READ["dataset"]


def test_encoding():
    initialize()
    assert PARSED["encoding"] == READ["encoding"]


def test_file_hash():
    initialize()
    assert PARSED["file_hash"] == READ["file_hash"]


def test_hash():
    initialize()
    assert PARSED["hash"] == READ["hash"]


def test_language():
    initialize()
    assert PARSED["language"] == READ["language"]


def test_mirror():
    initialize()
    assert PARSED["mirror"] == READ["mirror"]


def test_owner():
    initialize()
    assert PARSED["owner"] == READ["owner"]


def test_platform():
    initialize()
    assert PARSED["platform"] == READ["platform"]


def test_restored():
    initialize()
    assert PARSED["restored"] == READ["restored"]


def test_version():
    initialize()
    assert PARSED["version"] == READ["version"]


def test_chat():
    initialize()
    assert PARSED["chat"] == READ["chat"]


def test_diplomacy():
    initialize()
    assert PARSED["diplomacy"] == READ["diplomacy"]


def test_players():
    initialize()
    assert PARSED["players"] == READ["players"]


def test_profiles():
    initialize()
    assert PARSED["profiles"] == READ["profiles"]


def test_ratings():
    initialize()
    assert PARSED["ratings"] == READ["ratings"]


def test_teams():
    initialize()
    assert PARSED["teams"] == READ["teams"]


def test_achievements():
    initialize()
    assert PARSED["achievements"] == READ["achievements"]


def test_duration():
    initialize()
    assert PARSED["duration"] == READ["duration"]


def test_map():
    initialize()
    assert PARSED["map"] == READ["map"]


def test_objects():
    initialize()
    assert PARSED["objects"] == READ["objects"]


def test_postgame():
    initialize()
    assert PARSED["postgame"] == READ["postgame"]


def test_settings():
    initialize()
    assert PARSED["settings"] == READ["settings"]


def test_start_time():
    initialize()
    assert PARSED["start_time"] == READ["start_time"]
