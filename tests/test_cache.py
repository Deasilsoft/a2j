"""
Testing aoe2record-to-json caching.
"""

from tests.util import execute


def test_clean():
    data, err = execute([
        "curl",
        "http://localhost:8080/a2j/v1/clean/?record=test.mgz"
    ])

    if err is not None:
        print("Error while parsing from web API: ", err)

    assert data["success"] is True
    assert data["cleaned"] == 1


def test_clean_empty():
    data, err = execute([
        "curl",
        "http://localhost:8080/a2j/v1/clean/?record=test.mgz"
    ])

    if err is not None:
        print("Error while parsing from web API: ", err)

    assert data["success"] is True
    assert data["cleaned"] == 0
