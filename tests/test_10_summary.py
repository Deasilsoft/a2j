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
        response = client.get("/record/test.mgz/all/")
        cls.parsed = response.get_json()

        # OPEN DATA FILE
        with open(Path.cwd() / "tests" / "data" / "summary.json", "r") as file:
            # READ JSON FROM FILE
            cls.read = json.load(file)

    def assertPropertyEqual(self, property_name):
        parsed_value = self.parsed.get(property_name)
        read_value = self.read.get(property_name)

        self.assertEqual(parsed_value, read_value)

    def test_completed_property_equality(self):
        self.assertPropertyEqual("completed")

    def test_dataset_property_equality(self):
        self.assertPropertyEqual("dataset")

    def test_encoding_property_equality(self):
        self.assertPropertyEqual("encoding")

    def test_file_hash_property_equality(self):
        self.assertPropertyEqual("file_hash")

    def test_hash_property_equality(self):
        self.assertPropertyEqual("hash")

    def test_language_property_equality(self):
        self.assertPropertyEqual("language")

    def test_mirror_property_equality(self):
        self.assertPropertyEqual("mirror")

    def test_owner_property_equality(self):
        self.assertPropertyEqual("owner")

    def test_platform_property_equality(self):
        self.assertPropertyEqual("platform")

    def test_restored_property_equality(self):
        self.assertPropertyEqual("restored")

    def test_version_property_equality(self):
        self.assertPropertyEqual("version")

    def test_achievements_property_equality(self):
        self.assertPropertyEqual("achievements")

    def test_chat_property_equality(self):
        self.assertPropertyEqual("chat")

    def test_diplomacy_property_equality(self):
        self.assertPropertyEqual("diplomacy")

    def test_players_property_equality(self):
        self.assertPropertyEqual("players")

    def test_profiles_property_equality(self):
        self.assertPropertyEqual("profiles")

    def test_ratings_property_equality(self):
        self.assertPropertyEqual("ratings")

    def test_teams_property_equality(self):
        self.assertPropertyEqual("teams")

    def test_duration_property_equality(self):
        self.assertPropertyEqual("duration")

    def test_map_property_equality(self):
        self.assertPropertyEqual("map")

    def test_objects_property_equality(self):
        self.assertPropertyEqual("objects")

    def test_postgame_property_equality(self):
        self.assertPropertyEqual("postgame")

    def test_settings_property_equality(self):
        self.assertPropertyEqual("settings")

    def test_start_time_property_equality(self):
        self.assertPropertyEqual("start_time")


if __name__ == "__main__":
    unittest.main()
