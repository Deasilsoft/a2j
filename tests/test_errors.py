"""
Testing aoe2record-to-json errors.
"""

from tests.util import execute


def test_record_does_not_exist():
    data = execute([
        "curl",
        "http://localhost:8080/a2j/v1/parse/not-tested/?record=does-not-exist"
    ])

    assert len(data["errors"]) == 1

    assert len(data["errors"][0]) == 2
    assert data["errors"][0]["errno"] == 0
    assert data["errors"][0]["message"] == "Record does not exist: records/does-not-exist"


def test_command_does_not_exist():
    data = execute([
        "curl",
        "http://localhost:8080/a2j/v1/parse/not-real/fake-command/123/?record=test.mgz"
    ])

    assert len(data["errors"]) == 3

    assert len(data["errors"][0]) == 2
    assert data["errors"][0]["errno"] == 1
    assert data["errors"][0]["message"] == "Command does not exist: 123"

    assert len(data["errors"][1]) == 2
    assert data["errors"][1]["errno"] == 1
    assert data["errors"][1]["message"] == "Command does not exist: fake-command"

    assert len(data["errors"][2]) == 2
    assert data["errors"][2]["errno"] == 1
    assert data["errors"][2]["message"] == "Command does not exist: not-real"


def test_record_injection():
    data = execute([
        "curl",
        "http://localhost:8080/a2j/v1/parse/completed/?record=../injection.py"
    ])

    assert len(data["errors"]) == 1

    assert len(data["errors"][0]) == 2
    assert data["errors"][0]["errno"] == 100
    assert data["errors"][0]["message"] == "Injection attempt detected: ../injection.py"
