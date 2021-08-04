"""
Testing aoe2record-to-json caching.
"""

from tests.util import fetch


def test_clean():
    data, err = fetch([
        "curl",
        "-X",
        "DELETE",
        "http://localhost:8080/record/test.mgz/"
    ])

    if err is not None:
        print("Error while parsing from web API: ", err)

    assert data["deleted"] == 1


def test_clean_empty():
    data, err = fetch([
        "curl",
        "-X",
        "DELETE",
        "http://localhost:8080/record/test.mgz/"
    ])

    if err is not None:
        print("Error while parsing from web API: ", err)

    assert data["deleted"] == 0
