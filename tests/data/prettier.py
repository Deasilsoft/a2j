"""
https://github.com/Deasilsoft/a2j

Copyright (c) 2020-2023 Deasilsoft

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import json
from pathlib import Path

PREFIX = "temp_"
SUFFIX = ".json"


def prettier(name: str):
    with open(Path(__file__).parent / (name + SUFFIX), "r") as file:
        raw_json = json.load(file)

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
