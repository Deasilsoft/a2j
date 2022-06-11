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

        # GET CACHED DATA
        response = client.get("/record/test.mgz/all/?method=match")
        cls.parsed = response.get_json()

        # OPEN DATA FILE
        with open(Path.cwd() / "tests" / "data" / "match.json", "r") as file:
            # READ JSON FROM FILE
            cls.read = json.loads(file.read())

            # CLOSE FILE
            file.close()

    def test_data(self):
        # META
        assert self.parsed["completed"] == self.read["completed"]
        assert self.parsed["diplomacy_type"] == self.read["diplomacy_type"]
        assert self.parsed["file"] == self.read["file"]
        assert self.parsed["game_version"] == self.read["game_version"]
        assert self.parsed["guid"] == self.read["guid"]
        assert self.parsed["hash"] == self.read["hash"]
        assert self.parsed["log_version"] == self.read["log_version"]
        assert self.parsed["multiqueue"] == self.read["multiqueue"]
        assert self.parsed["save_version"] == self.read["save_version"]
        assert self.parsed["version"] == self.read["version"]

        # PLAYERS
        assert self.parsed["chat"] == self.read["chat"]
        assert self.parsed["players"] == self.read["players"]
        assert self.parsed["teams"] == self.read["teams"]

        # SETTINGS
        assert self.parsed["all_technologies"] == self.read["all_technologies"]
        assert self.parsed["cheats"] == self.read["cheats"]
        assert self.parsed["dataset"] == self.read["dataset"]
        assert self.parsed["difficulty"] == self.read["difficulty"]
        assert self.parsed["difficulty_id"] == self.read["difficulty_id"]
        assert self.parsed["lock_speed"] == self.read["lock_speed"]
        assert self.parsed["lock_teams"] == self.read["lock_teams"]
        assert self.parsed["map_reveal"] == self.read["map_reveal"]
        assert self.parsed["map_reveal_id"] == self.read["map_reveal_id"]
        assert self.parsed["population"] == self.read["population"]
        assert self.parsed["speed"] == self.read["speed"]
        assert self.parsed["speed_id"] == self.read["speed_id"]
        assert self.parsed["starting_age"] == self.read["starting_age"]
        assert self.parsed["starting_age_id"] == self.read["starting_age_id"]
        assert self.parsed["team_together"] == self.read["team_together"]
        assert self.parsed["type"] == self.read["type"]
        assert self.parsed["type_id"] == self.read["type_id"]

        # GAME
        assert self.parsed["actions"] == self.read["actions"]
        assert self.parsed["duration"] == self.read["duration"]
        assert self.parsed["gaia"] == self.read["gaia"]
        assert self.parsed["inputs"] == self.read["inputs"]
        assert self.parsed["lobby"] == self.read["lobby"]
        assert self.parsed["map"] == self.read["map"]
