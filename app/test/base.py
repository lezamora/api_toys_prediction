from flask_testing import TestCase
from manage import app


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('app.main.config.DevelopmentConfig')
        return app

    def setUp(self):
        pass

    def tearDown(self):
        pass
