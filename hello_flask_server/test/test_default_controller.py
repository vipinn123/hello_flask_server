# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from hello_flask_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_hello_swagger_get(self):
        """Test case for hello_swagger_get

        
        """
        query_string = [('first_name', 'first_name_example')]
        response = self.client.open(
            '/v1/helloSwagger',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
