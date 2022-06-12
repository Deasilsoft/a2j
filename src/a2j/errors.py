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


def no_record_error(message: str):
    """
    Record does not exist error.

    :param message:
    :return:
    """
    return {
        "message": "Record does not exist: " + message,
        "errno": 0,
    }


def invalid_commands_error(message: str):
    """
    Invalid commands error.

    :param message:
    :return:
    """

    return {
        "message": "Invalid commands: " + message,
        "errno": 1
    }


def parsing_record_error(message: str):
    """
    Parsing record error.

    :param message:
    :return:
    """

    return {
        "message": "Parsing record error: " + message,
        "errno": 2
    }


def no_commands_error():
    """
    No commands received error.

    :param message:
    :return:
    """

    return {
        "message": "No commands received.",
        "errno": 3
    }


def invalid_method_error(message: str):
    """
    Invalid method error.

    :param message:
    :return:
    """

    return {
        "message": "Invalid method: " + message,
        "errno": 4
    }
