import json
from pathlib import Path


def prettier(name):
    with open(Path(__file__).parent / (name + ".json"), "r") as read_file:
        with open(Path(__file__).parent / ("prettier_" + name + ".json"), "w") as write_file:
            write_file.write(json.dumps(json.loads(read_file.read()), indent=2, sort_keys=True))


prettier("summary")
prettier("match")


def overwrite(name):
    read_path = Path(__file__).parent / ("prettier_" + name + ".json")

    with open(read_path, "r") as read_file:
        with open(Path(__file__).parent / (name + ".json"), "w") as write_file:
            write_file.write(read_file.read())
            read_path.unlink()


overwrite("summary")
overwrite("match")
