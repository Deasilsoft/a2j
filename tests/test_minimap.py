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

import time
import unittest

from flask import Flask

from ..src import a2j
from ..src.routes import routes


class TestIndex(unittest.TestCase):
    """
    Test minimap.
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

    def test_minimap(self):
        response = self.client.get("/minimap/test.mgz/")

        assert response.mimetype == "image/png"
        assert response.status_code == 200

    def test_minimap_scale_1(self):
        response = self.client.get("/minimap/test.mgz/?scale=1")

        assert response.mimetype == "image/png"
        assert response.status_code == 200

    def test_minimap_scale_100(self):
        response = self.client.get("/minimap/test.mgz/?scale=100")

        assert response.mimetype == "image/png"
        assert response.status_code == 200

    def test_minimap_scale_string(self):
        response = self.client.get("/minimap/test.mgz/?scale=abc")

        assert response.mimetype == "image/png"
        assert response.status_code == 200
