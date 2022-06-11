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
import time
import unittest
from pathlib import Path

from flask import Flask

from ..src import a2j
from ..src.a2j.commands import available_commands
from ..src.routes import routes


class TestA2J(unittest.TestCase):
    """
    Test parsing of Age of Empires II record.
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup the testing environment.
        """

        # SETUP FLASK TEST ENVIRONMENT
        app = Flask(__name__)
        routes(app, time.time(), a2j.get_version())
        client = app.test_client()

        # CLEAR CACHE BEFORE TESTING
        client.delete("/record/test.mgz/")

        # PARSE DATA
        client.get("/record/test.mgz/" + "/".join(available_commands()) + "/")

        # GET CACHED DATA
        response = client.get("/record/test.mgz/" + "/".join(available_commands()) + "/")
        cls.parsed = response.get_json()

        # OPEN DATA FILE
        with open(Path.cwd() / "tests" / "data" / "test.json", "r") as file:
            # READ JSON FROM FILE
            cls.read = json.loads(file.read())

            # CLOSE FILE
            file.close()

    def test_data(self):
        # META
        assert self.parsed["completed"] == self.read["completed"]
        assert self.parsed["dataset"] == self.read["dataset"]
        assert self.parsed["encoding"] == self.read["encoding"]
        assert self.parsed["file_hash"] == self.read["file_hash"]
        assert self.parsed["hash"] == self.read["hash"]
        assert self.parsed["language"] == self.read["language"]
        assert self.parsed["mirror"] == self.read["mirror"]
        assert self.parsed["owner"] == self.read["owner"]
        assert self.parsed["platform"] == self.read["platform"]
        assert self.parsed["restored"] == self.read["restored"]
        assert self.parsed["version"] == self.read["version"]

        # PLAYERS
        assert self.parsed["achievements"] == self.read["achievements"]
        assert self.parsed["chat"] == self.read["chat"]
        assert self.parsed["diplomacy"] == self.read["diplomacy"]
        assert self.parsed["players"] == self.read["players"]
        assert self.parsed["profiles"] == self.read["profiles"]
        assert self.parsed["ratings"] == self.read["ratings"]
        assert self.parsed["teams"] == self.read["teams"]

        # GAME
        assert self.parsed["duration"] == self.read["duration"]
        assert self.parsed["map"] == self.read["map"]
        assert self.parsed["objects"] == self.read["objects"]
        assert self.parsed["postgame"] == self.read["postgame"]
        assert self.parsed["settings"] == self.read["settings"]
        assert self.parsed["start_time"] == self.read["start_time"]
