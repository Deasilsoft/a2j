"""
Testing aoe2record-to-json errors.
"""

from tests.util import fetch


def test_record_does_not_exist():
    data, err = fetch([
        "curl",
        "http://localhost:8080/record/does-not-exist/not-tested/"
    ])

    if err is not None:
        print("Error while parsing from web API: ", err)

    assert len(data["errors"]) == 1

    assert data["errors"][0]["errno"] == 0
    assert data["errors"][0]["message"] == "Record does not exist: /home/a2j/records/does-not-exist"


def test_command_does_not_exist():
    data, err = fetch([
        "curl",
        "http://localhost:8080/record/test.mgz/not-real/fake-command/123/version/"
    ])

    if err is not None:
        print("Error while parsing from web API: ", err)

    assert len(data["errors"]) == 1

    assert data["errors"][0]["errno"] == 1
    assert data["errors"][0]["message"] == "Invalid commands: ['123', 'fake-command', 'not-real']"


def test_record_injection():
    data, err = fetch([
        "curl",
        "http://localhost:8080/record/../injection.py/version/"
    ])

    if err is not None:
        print("Error while parsing from web API: ", err)

    assert data is None
