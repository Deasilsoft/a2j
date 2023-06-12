"""
https://github.com/Deasilsoft/a2j

Copyright (c) 2020-2023 Deasilsoft

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
from ..src.routes import routes


class TestCache(unittest.TestCase):
    """
    Test data caching.
    """

    client = None

    @classmethod
    def setUpClass(cls):
        """
        Setup the testing environment.
        """

        # SETUP FLASK TEST ENVIRONMENT
        app = Flask(__name__)
        routes(app, time.time())
        cls.client = app.test_client()

    def test_10_deletion_successful(self):
        response = self.client.delete("/record/test.mgz/")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["deleted"], 1)

    def test_20_deletion_empty(self):
        response = self.client.delete("/record/test.mgz/")
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["deleted"], 0)


if __name__ == "__main__":
    unittest.main()
