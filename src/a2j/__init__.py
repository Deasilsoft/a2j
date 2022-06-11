"""
https://github.com/Deasilsoft/a2j

Copyright (c) 2020-2022 Deasilsoft

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

from pathlib import Path
from typing import List

import mgz.summary

from . import cache, util
from .commands import summary_commands


def parse(record: str, command_list: List[str]) -> dict:
    """
    Parse Age of Empires II record and retrieve JSON object built on the user-supplied commands.

    :param (str) record: User-supplied record file.
    :param (List[str]) command_list: User-supplied commands.
    :return: JSON object
    :rtype: dict
    """

    data = {
        "errors": []
    }

    # SORT COMMANDS TO HAVE A REPEATABLE STRUCTURE OF THE JSON OBJECT
    command_list.sort()

    # IF COMMANDS CONTAIN ALL; CLEAR ALL OTHER COMMANDS
    if "all" in command_list:
        command_list = ["all"]

    # CHECK IF USER-SUPPLIED RECORD IS VALID
    if not util.is_record(record):
        data["errors"].append({
            "message": "Record does not exist: " + str(util.get_record(record)),
            "errno": 0,
        })

    # CHECK IF USER-SUPPLIED COMMANDS ARE EMPTY
    elif not command_list:
        data["errors"].append({
            "message": "No commands received.",
            "errno": 3
        })

    # CHECK IF USER-SUPPLIED COMMANDS ARE VALID
    elif not util.validate_commands(command_list):
        data["errors"].append({
            "message": "Invalid commands: " + str(util.invalid_commands(command_list)),
            "errno": 1
        })

    # OPEN THE RECORD FILE
    else:
        # FIRST GET CACHE IF AVAILABLE
        cached_data, is_cached = cache.read(record, command_list)

        if is_cached:
            data = cached_data

        else:
            with util.get_record(record).open(mode="rb") as file:
                summary = None

                try:
                    # SET THE LOGGER TO AN IMPOSSIBLY HIGH LEVEL TO PREVENT WEIRD OUTPUT
                    mgz.summary.logger.setLevel(9001)
                    summary = mgz.summary.FullSummary(file)

                except RuntimeError as err:
                    data["errors"].append({
                        "message": "Parsing AoE2 record stopped with this error: " + str(err),
                        "errno": 2
                    })

                # PUT THE RECORD DATA INSIDE OUR ARRAY
                if summary is not None:
                    # HANDLE SPECIAL ALL COMMAND
                    if "all" in command_list:
                        for command in summary_commands().keys():
                            if command != "all":
                                data[command] = summary_commands().get(command)(summary)

                    # HANDLE SUMMARY COMMANDS
                    else:
                        for command in util.valid_commands(command_list):
                            data[command] = summary_commands().get(command)(summary)

                file.close()

            # PUT TO CACHE
            cache.create(record, command_list, data)

    return data


def get_version() -> str:
    """
    Get the version of a2j.

    :return:  Version of a2j.
    :rtype: str
    """

    # OPEN VERSION FILE
    with open(Path.cwd() / "VERSION", "r") as file:
        # READ VERSION FROM FILE
        version = file.read().strip()

        # CLOSE FILE
        file.close()

    return version
