import json
import time

from flask import Response, Flask, request

from a2j.commands import get_commands
from a2j.encoder import JSONEncoder
from a2j.parse import parse
from a2j.version import version

app = Flask(__name__)
startTime = time.time()


@app.route("/a2j/", methods=["GET"])
def index() -> Response:
    return Response(json.dumps({
        "endpoints": ["v1"],
        "version": version(),
        "uptime": int(time.time() - startTime),
    }), mimetype="application/json")


@app.route("/a2j/v1/", methods=["GET"])
def v1() -> Response:
    return Response(json.dumps({
        "endpoints": ["parse"]
    }), mimetype="application/json")


@app.route("/a2j/v1/parse/", methods=["GET"])
def v1_parse_empty() -> Response:
    return Response(json.dumps({
        "endpoints": list(get_commands().keys()),
        "arguments": ["record"],
    }), mimetype="application/json")


@app.route("/a2j/v1/parse/<path:commands>/", methods=["GET"])
def v1_parse(commands: str) -> Response:
    endpoints = []
    commands = commands.split("/")

    for command in get_commands().keys():
        if command not in commands:
            endpoints.append(command)

    if "record" in request.args:
        data = parse(request.args.get("record"), commands)

        data["endpoints"] = endpoints
        data["arguments"] = []

        for argument in request.args.keys():
            if argument != "record":
                data["errors"].append({
                    "message": "Argument does not exist: " + argument,
                    "errno": 3
                })

        return Response(json.dumps(data, cls=JSONEncoder), mimetype="application/json")

    else:
        return Response(json.dumps({
            "endpoints": endpoints,
            "arguments": ["record"],
        }), mimetype="application/json")


app.run(host="0.0.0.0", debug=False, port=8080)
