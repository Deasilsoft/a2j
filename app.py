import json
import time

from flask import Response, Flask, request

from a2j.commands import get_commands
from a2j.parse import parse
from a2j.version import version

app = Flask(__name__)
startTime = time.time()


@app.route("/a2j/", methods=["GET"])
def index():
    return Response(json.dumps({
        "endpoints": ["v1"],
        "version": version(),
        "uptime": int(time.time() - startTime),
    }), mimetype="application/json")


@app.route("/a2j/v1/", methods=["GET"])
def v1():
    return Response(json.dumps({
        "endpoints": ["parse"]
    }), mimetype="application/json")


@app.route("/a2j/v1/parse/", methods=["GET"])
def v1_parse():
    return Response(json.dumps({
        "endpoints": list(get_commands().keys()),
        "parameters": ["record"],
    }), mimetype="application/json")


@app.route("/a2j/v1/parse/<path:commands>/", methods=["GET"])
def v1_parse_commands(commands):
    if "record" in request.args:
        return Response(parse(request.args.get("record"), commands.split("/")), mimetype="application/json")
    else:
        return Response(json.dumps({
            "parameters": ["record"],
        }), mimetype="application/json")


app.run(debug=False, port=4000)
