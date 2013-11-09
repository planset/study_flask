import unittest

from flaskr.core import db
from flaskr.frontend import create_app

from . import config

class FlaskTestCaseMixin(object):
    def _request(self, method, *args, **kwargs):
        kwargs.setdefault('content_type', 'text/html')
        kwargs.setdefault('follow_redirects', True)
        return method(*args, **kwargs)

    def get(self, *args, **kwargs):
        return self._request(self.client.get, *args, **kwargs)

    def post(self, *args, **kwargs):
        return self._request(self.client.post, *args, **self._html_data(kwargs))


class FlaskrTestCase(FlaskTestCaseMixin, unittest.TestCase):
    def _create_app(self):
        return create_app(config)

    def setUp(self):
        super(FlaskrTestCase, self).setUp()
        self.app = self._create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        super(FlaskrTestCase, self).tearDown()
        db.drop_all()

