"""
https://github.com/Deasilsoft/a2j

Copyright (c) 2020-2021 Deasilsoft

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
        cls.parsed = client.get("/record/test.mgz/" + "/".join(available_commands()) + "/").get_json()

        # OPEN DATA FILE
        with open(Path.cwd() / "tests" / "data" / "test.json", "r") as file:
            # READ JSON FROM FILE
            cls.read = json.loads(file.read())

            # CLOSE FILE
            file.close()

    def test_completed(self):
        assert self.parsed["completed"] == self.read["completed"]

    def test_dataset(self):
        assert self.parsed["dataset"] == self.read["dataset"]

    def test_encoding(self):
        assert self.parsed["encoding"] == self.read["encoding"]

    def test_file_hash(self):
        assert self.parsed["file_hash"] == self.read["file_hash"]

    def test_hash(self):
        assert self.parsed["hash"] == self.read["hash"]

    def test_language(self):
        assert self.parsed["language"] == self.read["language"]

    def test_mirror(self):
        assert self.parsed["mirror"] == self.read["mirror"]

    def test_owner(self):
        assert self.parsed["owner"] == self.read["owner"]

    def test_platform(self):
        assert self.parsed["platform"] == self.read["platform"]

    def test_restored(self):
        assert self.parsed["restored"] == self.read["restored"]

    def test_version(self):
        assert self.parsed["version"] == self.read["version"]

    def test_chat(self):
        assert self.parsed["chat"] == self.read["chat"]

    def test_diplomacy(self):
        assert self.parsed["diplomacy"] == self.read["diplomacy"]

    def test_players(self):
        assert self.parsed["players"] == self.read["players"]

    def test_profiles(self):
        assert self.parsed["profiles"] == self.read["profiles"]

    def test_ratings(self):
        assert self.parsed["ratings"] == self.read["ratings"]

    def test_teams(self):
        assert self.parsed["teams"] == self.read["teams"]

    def test_achievements(self):
        assert self.parsed["achievements"] == self.read["achievements"]

    def test_duration(self):
        assert self.parsed["duration"] == self.read["duration"]

    def test_map(self):
        assert self.parsed["map"] == self.read["map"]

    def test_objects(self):
        assert self.parsed["objects"] == self.read["objects"]

    def test_postgame(self):
        assert self.parsed["postgame"] == self.read["postgame"]

    def test_settings(self):
        assert self.parsed["settings"] == self.read["settings"]

    def test_start_time(self):
        assert self.parsed["start_time"] == self.read["start_time"]
