import json
from pathlib import Path

PREFIX = "temp_"
SUFFIX = ".json"


def prettier(name: str):
    with open(Path(__file__).parent / (name + SUFFIX), "r") as file:
        raw_json = json.loads(file.read())

    with open(Path(__file__).parent / (PREFIX + name + SUFFIX), "w") as file:
        pretty_json = json.dumps(
            raw_json,
            indent=2,
            sort_keys=True,
        )

        file.write(pretty_json)


def overwrite(name: str):
    path = Path(__file__).parent / (PREFIX + name + SUFFIX)

    with open(path, "r") as file:
        pretty_json = file.read()

    with open(Path(__file__).parent / (name + SUFFIX), "w") as file:
        file.write(pretty_json)
        path.unlink()


prettier("summary")
prettier("match")

overwrite("summary")
overwrite("match")
