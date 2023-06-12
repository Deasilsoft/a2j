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

import _hashlib
import codecs
import inspect
import json
import types
from datetime import timedelta
from enum import Enum

import mgz
import mgz.summary
from mgz.model import Player


class JSONEncoder(json.JSONEncoder):
    """
    A JSONEncoder for parsing Age of Empires II records.
    """

    def default(self, obj: any) -> any:
        """
        :param obj: The object to convert to something JSON-friendly.
        :rtype:
        """

        if isinstance(obj, _hashlib.HASH):
            return {
                "type": obj.name,
                "hex": obj.hexdigest(),
            }

        if isinstance(obj, mgz.Version):
            return {
                "name": obj.name,
                "value": obj.value,
            }

        if isinstance(obj, mgz.summary.full.Chat):
            return {
                "name": obj.name,
                "value": obj.value,
            }

        if isinstance(obj, (set, frozenset)):
            return list(obj)

        if isinstance(obj, bytes):
            return obj.decode("unicode_escape")

        if isinstance(obj, (codecs.CodecInfo, Enum)):
            return obj.name

        if isinstance(obj, timedelta):
            return str(obj)

        if isinstance(obj, types.MappingProxyType):
            return dict(obj)

        if inspect.isbuiltin(obj):
            if obj.__name__ in ["latin_1_encode", "latin_1_decode"]:
                return ""

        if isinstance(obj, Player):
            # TODO: support team once the Circularity Error has been resolved
            obj.team = None

            return obj.__dict__

        if hasattr(obj, "__dict__"):
            return obj.__dict__

        return json.JSONEncoder.default(self, obj)
