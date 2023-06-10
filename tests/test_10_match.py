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
        routes(app, time.time())
        client = app.test_client()

        # CLEAR CACHE BEFORE TESTING
        client.delete("/record/test.mgz/")

        # GET CACHED DATA
        response = client.get("/record/test.mgz/all/?method=match")
        cls.parsed = response.get_json()

        # OPEN DATA FILE
        with open(Path.cwd() / "tests" / "data" / "match.json", "r") as file:
            # READ JSON FROM FILE
            cls.read = json.load(file)

    def assertPropertyEqual(self, property_name):
        parsed_value = self.parsed.get(property_name)
        read_value = self.read.get(property_name)

        self.assertEqual(parsed_value, read_value)

    def test_completed_property_equality(self):
        self.assertPropertyEqual("completed")

    def test_file_property_equality(self):
        self.assertPropertyEqual("file")

    def test_game_version_property_equality(self):
        self.assertPropertyEqual("game_version")

    def test_guid_property_equality(self):
        self.assertPropertyEqual("guid")

    def test_hash_property_equality(self):
        self.assertPropertyEqual("hash")

    def test_log_version_property_equality(self):
        self.assertPropertyEqual("log_version")

    def test_multiqueue_property_equality(self):
        self.assertPropertyEqual("multiqueue")

    def test_save_version_property_equality(self):
        self.assertPropertyEqual("save_version")

    def test_version_property_equality(self):
        self.assertPropertyEqual("version")

    def test_chat_property_equality(self):
        self.assertPropertyEqual("chat")

    def test_players_property_equality(self):
        self.assertPropertyEqual("players")

    def test_teams_property_equality(self):
        self.assertPropertyEqual("teams")

    def test_all_technologies_property_equality(self):
        self.assertPropertyEqual("all_technologies")

    def test_cheats_property_equality(self):
        self.assertPropertyEqual("cheats")

    def test_dataset_property_equality(self):
        self.assertPropertyEqual("dataset")

    def test_difficulty_property_equality(self):
        self.assertPropertyEqual("difficulty")

    def test_difficulty_id_property_equality(self):
        self.assertPropertyEqual("difficulty_id")

    def test_diplomacy_type_property_equality(self):
        self.assertPropertyEqual("diplomacy_type")

    def test_lock_speed_property_equality(self):
        self.assertPropertyEqual("lock_speed")

    def test_lock_teams_property_equality(self):
        self.assertPropertyEqual("lock_teams")

    def test_map_reveal_property_equality(self):
        self.assertPropertyEqual("map_reveal")

    def test_map_reveal_id_property_equality(self):
        self.assertPropertyEqual("map_reveal_id")

    def test_population_property_equality(self):
        self.assertPropertyEqual("population")

    def test_speed_property_equality(self):
        self.assertPropertyEqual("speed")

    def test_speed_id_property_equality(self):
        self.assertPropertyEqual("speed_id")

    def test_starting_age_property_equality(self):
        self.assertPropertyEqual("starting_age")

    def test_starting_age_id_property_equality(self):
        self.assertPropertyEqual("starting_age_id")

    def test_team_together_property_equality(self):
        self.assertPropertyEqual("team_together")

    def test_type_property_equality(self):
        self.assertPropertyEqual("type")

    def test_type_id_property_equality(self):
        self.assertPropertyEqual("type_id")


if __name__ == "__main__":
    unittest.main()
