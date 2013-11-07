import unittest
from flaskr.factory import create_app
from flaskr.models import Entry, User, db

from . import config


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(__name__, config)
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.drop_all()
        self.app_context.pop()

    def test_empty_db(self):
        rv = self.client.get('/')
        assert 'No entries here so far' in rv.data

    def test_post_entry(self):
        user = User(username='testuser', password='testuser')
        db.session.add(user)
        db.session.commit()

        response = self.client.post('/login',
                data={'username':'testuser', 
                    'password':'testuser'},
                follow_redirects=False)

        response = self.client.post('/add',
                               data={'title': 'test title 1', 'text': 'test text 1'},
                               follow_redirects=True)
        assert response.status_code == 200
        assert "test title 1" in response.data
        assert "test text 1" in response.data
        with self.app.test_request_context():
            assert Entry.query.count() == 1
            entry = Entry.query.get(1)
            entry.title = 'test title 1'
            entry.text = 'test text 1'

if __name__ == '__main__':
    unittest.main()

