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

import json
import os
import time
from io import BytesIO

from flask import Flask, request, Response, send_file

from .a2j import create_minimap, delete_cache, get_match_commands, get_summary_commands, get_version, handle_record, is_record, JSONEncoder, no_record_error, parse_record


def routes(app: Flask, start_time: float):
    """
    Get all a2j routes.

    :param (Flask) app: The a2j Flask app.
    :param (float) start_time: The start time of the a2j app.
    :param (str) version: The version of the a2j app.
    :return:
    """

    @app.route("/", methods=["GET"])
    def get_index() -> Response:
        """
        Handle Endpoint: GET /

        :return: HTTP Response.
        :rtype: Response
        """

        return Response(json.dumps({
            "version": get_version(),
            "uptime": time.time() - start_time,
            "environment": os.getenv("FLASK_ENV"),
            "endpoints": ["record", "minimap"]
        }), mimetype="application/json")

    @app.route("/minimap", methods=["GET"])
    @app.route("/minimap/", methods=["GET"])
    @app.route("/minimap/<path:path>", methods=["GET"])
    @app.route("/minimap/<path:path>/", methods=["GET"])
    def get_minimap(path: str = "") -> Response:
        """
        Handle Endpoint: GET /minimap/<path:path>

            <path:path> The path with record.

        :return: HTTP Response.
        :rtype: Response
        """

        # GET RECORD
        record = handle_record(path.split("/")[0])

        # IF RECORD EXISTS
        if record != "" and is_record(record):

            # SET SCALE FROM USER-INPUT
            if "scale" in request.args and request.args.get("scale").isdigit():
                scale = int(request.args.get("scale"))

            # DEFAULT SCALE
            else:
                scale = 5

            # PREPARE IMAGE
            img = BytesIO()

            # CREATE MINIMAP IMAGE
            create_minimap(record, scale).save(img, "PNG", quality=100)

            img.seek(0)

            return send_file(img, mimetype="image/png", download_name=record + ".minimap.png")

        # OTHERWISE: OUTPUT ERROR
        return Response(json.dumps({
            "errors": [no_record_error(record)]
        }), mimetype="application/json")

    @app.route("/record", methods=["GET"])
    @app.route("/record/", methods=["GET"])
    @app.route("/record/<path:path>", methods=["GET"])
    @app.route("/record/<path:path>/", methods=["GET"])
    def get_record(path: str = "") -> Response:
        """
        Handle Endpoint: GET /record/<path:path>

            <path:path> The path with record and commands.

        :return: HTTP Response.
        :rtype: Response
        """

        # GET RECORD
        record = handle_record(path.split("/")[0])

        # FILTER EMPTY COMMANDS
        commands = [c for c in path.split("/")[1:] if c != ""]

        # SET PARSE METHOD FROM USER-INPUT
        if "method" in request.args and request.args.get("method").isalpha():
            method = str(request.args.get("method"))

        # DEFAULT PARSE METHOD
        else:
            method = "summary"

        # PARSE DATA
        data = parse_record(record, commands, method)

        # NOT ALL
        if "all" not in commands:

            # FILL ENDPOINTS WITH MISSING SUMMARY COMMANDS
            if method == "summary":
                data["endpoints"] = [c for c in get_summary_commands() if c not in commands]

            # FILL ENDPOINTS WITH MISSING MATCH COMMANDS
            elif method == "match":
                data["endpoints"] = [c for c in get_match_commands() if c not in commands]

        # IS ALL
        else:
            data["endpoints"] = []

        return Response(json.dumps(data, cls=JSONEncoder), mimetype="application/json")

    @app.route("/record", methods=["DELETE"])
    @app.route("/record/", methods=["DELETE"])
    @app.route("/record/<path:path>", methods=["DELETE"])
    @app.route("/record/<path:path>/", methods=["DELETE"])
    def delete_record(path: str = "") -> Response:
        """
        Handle Endpoint: DELETE /record/<string:record>

            <path:path> The path with record.

        :return: HTTP Response.
        :rtype: Response
        """

        # GET RECORD
        record = handle_record(path.split("/")[0])

        # IF RECORD EXISTS
        if record != "" and is_record(record):
            return Response(json.dumps({
                "deleted": delete_cache(record)
            }), mimetype="application/json")

        # OTHERWISE: OUTPUT ERROR
        return Response(json.dumps({
            "errors": [no_record_error(record)]
        }), mimetype="application/json")
