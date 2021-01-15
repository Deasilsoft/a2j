"""
aoe2record-to-json JSONEncoder class.
"""
import _hashlib
import json

import mgz
import mgz.summary


class JSONEncoder(json.JSONEncoder):
    """A JSONEncoder for parsing Age of Empires II records."""

    def default(self, obj: any) -> any:
        """
        :param obj:
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

        if isinstance(obj, mgz.summary.chat.Chat):
            return {
                "name": obj.name,
                "value": obj.value,
            }

        if isinstance(obj, bytes):
            return obj.decode("unicode_escape")

        return json.JSONEncoder.default(self, obj)
