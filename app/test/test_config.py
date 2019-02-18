import unittest

from flask import current_app
from app.test.base import BaseTestCase

from manage import app


class TestDevelopmentConfig(BaseTestCase):

    def test_app_is_development(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertEqual(app.config['SERVER_NAME'], 'localhost:7070')


if __name__ == '__main__':
    unittest.main()
