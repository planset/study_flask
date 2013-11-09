from . import FlaskrTestCase

class EntriesTestCase(FlaskrTestCase):
    def test_index(self):
        r = self.get('/')
        self.assertEquals(304, r.status_code)

    def test_show_entries(self):
        r = self.get('/entries/')
        self.assertEquals(304, r.status_code)


