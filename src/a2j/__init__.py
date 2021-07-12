"""
https://github.com/Deasilsoft/a2j

Copyright (c) 2020-2021 Deasilsoft

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
import mgz.summary

from . import cache
from . import util
from .commands import get_commands


def parse(record: str, commands: list) -> dict:
    """
    Parse Age of Empires II record and retrieve JSON object built on the user-supplied commands.

    :param (str) record: User-supplied record file.
    :param (list) commands: User-supplied commands.
    :return: JSON object
    :rtype: dict
    """
    data = {
        "errors": []
    }

    # SORT COMMANDS TO HAVE A REPEATABLE STRUCTURE OF THE JSON OBJECT
    commands.sort()

    # CHECK IF USER-INPUT IS VALID; THEN OPEN THE RECORD FILE
    if util.is_record(record):

        # FIRST GET CACHE IF AVAILABLE
        cached_data, is_cached = cache.read(record, commands)

        if is_cached:
            data = cached_data

        else:
            try:
                with util.record(record).open(mode="rb") as file:
                    perform = False

                    # CHECK IF ANY COMMAND IS VALID; TO PREVENT PARSING THE RECORD WITH NO OUTPUT
                    for command in commands:
                        if command in get_commands():
                            perform = True

                        else:
                            data["errors"].append({
                                "message": "Command does not exist: " + command,
                                "errno": 1
                            })

                    # GO AHEAD AND PERFORM THE RECORD PARSING
                    if perform:
                        summary = None

                        try:
                            # SET THE LOGGER TO AN IMPOSSIBLY HIGH LEVEL TO PREVENT WEIRD OUTPUT
                            mgz.summary.LOGGER.setLevel(9001)
                            summary = mgz.summary.Summary(file)

                        except Exception as e:
                            data["errors"].append({
                                "message": "Parsing AoE2 record stopped with this error: " + str(e),
                                "errno": 2
                            })

                        # PUT THE RECORD DATA INSIDE OUR ARRAY
                        if summary is not None:
                            for command in commands:
                                if command in get_commands():
                                    data[command] = get_commands().get(command)(summary)

                    file.close()

            except FileNotFoundError as e:
                data["errors"].append({
                    "message": "Record does not exist: " + e.filename,
                    "errno": 0
                })

            # PUT TO CACHE
            cache.create(record, commands, data)

    else:
        data["errors"].append({
            "message": "Injection attempt detected: " + record,
            "errno": 100
        })

    return data
