# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import unittest

import webtest

import testapp


class TestCase(unittest.TestCase):
    def test_get(self):
        app = webtest.TestApp(testapp.application)
        resp = app.get('/')
        self.assertEqual(200, resp.status_int)
        self.assertEqual('application/json', resp.content_type)
        self.assertEqual({'message': 'something'}, resp.json)
