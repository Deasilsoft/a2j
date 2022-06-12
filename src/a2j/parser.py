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

from typing import List

import mgz.model
import mgz.summary

from .cache import create_cache, read_cache
from .errors import invalid_commands_error, invalid_method_error, no_commands_error, no_record_error, parsing_record_error
from .util import get_invalid_commands, get_match_commands, get_record_path, get_summary_commands, get_valid_commands, is_record, is_valid_command, is_valid_method


def parse_record(record: str, command_list: List[str], method: str = "summary") -> dict:
    """
    Parse Age of Empires II record and retrieve JSON object built on the user-supplied commands.

    :param (str) record: User-supplied record file.
    :param (List[str]) command_list: User-supplied commands.
    :param (str) method: User-supplied method.
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
    if record == "" or not is_record(record):
        data["errors"].append(no_record_error(record))

    # CHECK IF USER-SUPPLIED COMMANDS ARE EMPTY
    if not command_list:
        data["errors"].append(no_commands_error())

    # CHECK IF USER-SUPPLIED METHOD IS VALID
    if not is_valid_method(method):
        data["errors"].append(invalid_method_error(method))

    # CHECK IF USER-SUPPLIED COMMANDS ARE VALID
    elif not is_valid_command(command_list, method):
        data["errors"].append(invalid_commands_error(str(get_invalid_commands(command_list, method))))

    # OPEN THE RECORD FILE
    if not data["errors"]:
        # FIRST GET CACHE IF AVAILABLE
        cached_data, is_cached = read_cache(record, command_list, method)

        if is_cached:
            data = cached_data

        else:
            with get_record_path(record).open(mode="rb") as file:
                # HANDLE SUMMARY METHOD
                if method == "summary":
                    summary = None

                    try:
                        # SET THE LOGGER TO AN IMPOSSIBLY HIGH LEVEL TO PREVENT WEIRD OUTPUT
                        mgz.summary.logger.setLevel(9001)
                        summary = mgz.summary.FullSummary(file)

                    except RuntimeError as err:
                        data["errors"].append(parsing_record_error(str(err)))

                    # PUT THE RECORD DATA INSIDE OUR ARRAY
                    if summary is not None:
                        # HANDLE SPECIAL ALL COMMAND
                        if "all" in command_list:
                            for command in get_summary_commands().keys():
                                if command != "all":
                                    data[command] = get_summary_commands().get(command)(summary)

                        # HANDLE SUMMARY COMMANDS
                        else:
                            for command in get_valid_commands(command_list, method):
                                data[command] = get_summary_commands().get(command)(summary)

                # HANDLE MATCH METHOD
                elif method == "match":
                    match = None

                    try:
                        match = mgz.model.parse_match(file)

                    except RuntimeError as err:
                        data["errors"].append(parsing_record_error(str(err)))

                    # PUT THE RECORD DATA INSIDE OUR ARRAY
                    if match is not None:
                        # HANDLE SPECIAL ALL COMMAND
                        if "all" in command_list:
                            for command in get_match_commands():
                                if command != "all":
                                    data[command] = getattr(match, command)

                        # HANDLE MATCH COMMANDS
                        else:
                            for command in get_valid_commands(command_list, method):
                                data[command] = getattr(match, command)

                file.close()

            # PUT TO CACHE
            create_cache(record, command_list, method, data)

    return data
