"""
The a2j app.
"""
import json
import time
from pathlib import Path

from flask import Response, Flask

import a2j
import a2j.cache
import a2j.encoder
import a2j.util

app = Flask(__name__)
start_time = time.time()

# READ VERSION
with open(Path.cwd() / "VERSION", "r") as file:
    version = file.read().strip()


@app.route("/", methods=["GET"])
def get_index() -> Response:
    """
    Handle Endpoint: GET /

    :return: HTTP Response.
    :rtype: Response
    """

    return Response(json.dumps({
        "version": version,
        "uptime": time.time() - start_time,
        "endpoints": ["record"]
    }), mimetype="application/json")


@app.route("/record/<path:path>", methods=["GET"])
def get_record(path: str) -> Response:
    """
    Handle Endpoint: GET /record/<path:path>

        <path:path> The path with record and commands data.

    :return: HTTP Response.
    :rtype: Response
    """

    # GET RECORD
    record = path.split("/")[0]

    # SPLIT COMMANDS
    commands = path.split("/")[1:]

    # FILTER EMPTY COMMANDS
    commands = list(filter(lambda command: command != "", commands))

    # PARSE DATA
    data = a2j.parse(record, commands)

    # FILL ENDPOINTS WITH MISSING COMMANDS
    data["endpoints"] = [command for command in a2j.available_commands() if command not in commands]

    return Response(json.dumps(data, cls=a2j.encoder.JSONEncoder), mimetype="application/json")


@app.route("/record/<path:path>", methods=["DELETE"])
def delete_record(path: str) -> Response:
    """
    Handle Endpoint: DELETE /record/<string:record>

    :return: HTTP Response.
    :rtype: Response
    """

    # GET RECORD
    record = path.split("/")[0]

    # IF RECORD EXISTS
    if a2j.util.is_record(record):
        return Response(json.dumps({
            "deleted": a2j.cache.delete(record)
        }), mimetype="application/json")

    # OTHERWISE: OUTPUT ERROR
    return Response(json.dumps({
        "errors": [{
            "message": "Record doesn't exist.",
            "errno": 0,
        }]
    }), mimetype="application/json")


# START THE APPLICATION ON PORT 8080
app.run(host="0.0.0.0", debug=False, port=8080)
