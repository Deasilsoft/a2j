"""
The a2j app.

TODO: make RESTFUL
"""
import json
import time
from pathlib import Path

from flask import Response, Flask, request

import a2j
import a2j.cache
import a2j.commands
import a2j.encoder
import a2j.util

app = Flask(__name__)
startTime = time.time()

with open(Path(__file__).parent.parent.resolve() / "VERSION", "r") as file:
    version = file.read().strip()


@app.route("/a2j/", methods=["GET"])
def index() -> Response:
    """
    Handle Endpoint: /a2j/

    :return: HTTP Response.
    :rtype: Response
    """
    return Response(json.dumps({
        "endpoints": ["v1"],
        "version": version,
        "uptime": time.time() - startTime,
    }), mimetype="application/json")


@app.route("/a2j/v1/", methods=["GET"])
def v1() -> Response:
    """
    Handle Endpoint: /a2j/v1/

    :return: HTTP Response.
    :rtype: Response
    """
    return Response(json.dumps({
        "endpoints": ["parse", "clean"]
    }), mimetype="application/json")


@app.route("/a2j/v1/parse/", methods=["GET"])
def v1_parse_empty() -> Response:
    """
    Handle Endpoint: /a2j/v1/parse/

    :return: HTTP Response.
    :rtype: Response
    """
    return Response(json.dumps({
        "endpoints": list(a2j.commands.get_commands().keys()),
        "arguments": ["record"],
    }), mimetype="application/json")


@app.route("/a2j/v1/clean/", methods=["GET"])
def v1_clean() -> Response:
    """
    Handle Endpoint: /a2j/v1/clean/

    :return: HTTP Response.
    :rtype: Response
    """
    if "record" in request.args:
        record = request.args.get("record")

        return Response(json.dumps({
            "endpoints": [],
            "arguments": [],
            "success": a2j.util.is_record(record),
            "cleaned": a2j.cache.delete(record)
        }), mimetype="application/json")

    return Response(json.dumps({
        "endpoints": [],
        "arguments": ["record"],
        "success": False,
        "cleaned": 0
    }), mimetype="application/json")


@app.route("/a2j/v1/parse/<path:commands>/", methods=["GET"])
def v1_parse(commands: str) -> Response:
    """
    Handle Endpoint: /a2j/v1/parse/<path:commands>/

        <path:command> returns a string with all directories--the path--leading to the trailing file separator.

    :return: HTTP Response.
    :rtype: Response
    """
    endpoints = []
    commands = commands.split("/")

    for command in a2j.commands.get_commands().keys():
        if command not in commands:
            endpoints.append(command)

    if "record" in request.args:
        record = request.args.get("record")
        data = a2j.parse(record, commands)

        data["endpoints"] = endpoints
        data["arguments"] = []

        for arg in request.args.keys():
            if arg != "record":
                data["errors"].append({
                    "message": "Argument does not exist: " + arg,
                    "errno": 3
                })

        return Response(json.dumps(data, cls=a2j.encoder.JSONEncoder), mimetype="application/json")

    return Response(json.dumps({
        "endpoints": endpoints,
        "arguments": ["record"],
    }), mimetype="application/json")


# START THE APPLICATION ON PORT 8080
app.run(host="0.0.0.0", debug=False, port=8080)
