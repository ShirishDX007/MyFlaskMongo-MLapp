import unittest
from app import app, load_data


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_load_data_route(self):
        response = self.app.get('/load_data')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Data loaded into MongoDB.', response.data)


if __name__ == '__main__':
    unittest.main()