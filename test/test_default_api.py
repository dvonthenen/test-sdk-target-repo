# coding: utf-8

"""
    Sample API

    Optional multiline or single-line description in [CommonMark](http://commonmark.org/help/) or HTML.  # noqa: E501

    OpenAPI spec version: 0.1.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.default_api import DefaultApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_users_get(self):
        """Test case for users_get

        Returns a list of users.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
