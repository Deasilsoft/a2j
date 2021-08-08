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

import time
import unittest

from flask import Flask

from ..src import a2j
from ..src.routes import routes


class TestErrors(unittest.TestCase):
    """
    Test errors handling.
    """

    @classmethod
    def setUpClass(cls):
        """
        Setup the testing environment.
        """

        # SETUP FLASK TEST ENVIRONMENT
        app = Flask(__name__)
        routes(app, time.time(), a2j.get_version())
        cls.client = app.test_client()

    def test_record_does_not_exist(self):
        data = self.client.get("/record/does-not-exist/not-tested/").get_json()

        assert len(data["errors"]) == 1

        assert data["errors"][0]["errno"] == 0
        assert data["errors"][0]["message"] == "Record does not exist: /home/a2j/records/does-not-exist"

    def test_record_injection(self):
        data = self.client.get("/record/../injection.py/version/").get_json()

        assert len(data["errors"]) == 1

        assert data["errors"][0]["errno"] == 0
        assert data["errors"][0]["message"] == "Record does not exist: /home/a2j/records/.."

    def test_record_deletion_failure(self):
        data = self.client.delete("/record/does-not-exist/").get_json()

        assert len(data["errors"]) == 1

        assert data["errors"][0]["errno"] == 0
        assert data["errors"][0]["message"] == "Record does not exist: /home/a2j/records/does-not-exist"

    def test_command_does_not_exist(self):
        data = self.client.get("/record/test.mgz/not-real/fake-command/123/version/").get_json()

        assert len(data["errors"]) == 1

        assert data["errors"][0]["errno"] == 1
        assert data["errors"][0]["message"] == "Invalid commands: ['123', 'fake-command', 'not-real']"

    def test_commands_are_empty(self):
        data = self.client.get("/record/test.mgz/").get_json()

        assert len(data["errors"]) == 1

        assert data["errors"][0]["errno"] == 3
        assert data["errors"][0]["message"] == "No commands received."
