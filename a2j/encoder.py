import _hashlib
import json

import mgz
import mgz.summary


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, _hashlib.HASH):
            return {
                "type": obj.name,
                "hex": obj.hexdigest(),
            }

        elif isinstance(obj, mgz.Version):
            return {
                "name": obj.name,
                "value": obj.value,
            }

        elif isinstance(obj, mgz.summary.chat.Chat):
            return {
                "name": obj.name,
                "value": obj.value,
            }

        elif isinstance(obj, bytes):
            return obj.decode("unicode_escape")

        return json.JSONEncoder.default(self, obj)
