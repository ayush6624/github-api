import unittest
from app import app


class BasicTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page_test(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 404)

    def test_api_popular_test(self):
        result = self.app.get('/popular')
        self.assertEqual(result.status_code, 200)

    def test_error_check(self):
        result = self.app.get('/contributor/ayush6624/false-repo-name')
        self.assertEqual(result.status_code, 400)


if __name__ == "__main__":
    unittest.main()
