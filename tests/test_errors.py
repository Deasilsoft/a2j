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
        path = "/record/does-not-exist/not-tested/"
        errno = 0
        message = "Record does not exist: /home/a2j/records/does-not-exist"

        self._test_error(path, errno, message, self.client.get)

    def test_record_direct_path_injection(self):
        path = "/record/../injection.py/version/"
        errno = 0
        message = "Record does not exist: /home/a2j/records/.."

        self._test_error(path, errno, message, self.client.get)

    def test_record_traversal_encoding_path_injection(self):
        path = "/record/%2e%2e%2finjection.py/version/"
        errno = 0
        message = "Record does not exist: /home/a2j/records/.."

        self._test_error(path, errno, message, self.client.get)

    def test_record_deletion_failure(self):
        path = "/record/does-not-exist/"
        errno = 0
        message = "Record does not exist: /home/a2j/records/does-not-exist"

        self._test_error(path, errno, message, self.client.delete)

    def test_command_does_not_exist(self):
        path = "/record/test.mgz/not-real/fake-command/123/version/"
        errno = 1
        message = "Invalid commands: ['123', 'fake-command', 'not-real']"

        self._test_error(path, errno, message, self.client.get)

    def test_commands_are_empty(self):
        path = "/record/test.mgz/"
        errno = 3
        message = "No commands received."

        self._test_error(path, errno, message, self.client.get)

    def test_minimap_does_not_exist(self):
        path = "/minimap/does-not-exist/not-tested/"
        errno = 0
        message = "Record does not exist: /home/a2j/records/does-not-exist"

        self._test_error(path, errno, message, self.client.get)

    @staticmethod
    def _test_error(path: str, errno: int, message: str, function: callable):
        data = function(path).get_json()

        assert len(data["errors"]) == 1
        assert data["errors"][0]["errno"] == errno
        assert data["errors"][0]["message"] == message
