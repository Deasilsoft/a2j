"""
Testing aoe2record-to-json caching.
"""

from tests.util import execute


def test_clean():
    data = execute([
        "curl",
        "http://localhost:8080/a2j/v1/clean/?record=test.mgz"
    ])

    assert data["success"] is True
    assert data["cleaned"] == 1


def test_clean_empty():
    data = execute([
        "curl",
        "http://localhost:8080/a2j/v1/clean/?record=test.mgz"
    ])

    assert data["success"] is True
    assert data["cleaned"] == 0
