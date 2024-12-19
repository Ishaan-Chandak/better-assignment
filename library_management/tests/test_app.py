import unittest
from app import app

class LibraryManagementTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.headers = {"Authorization": "Bearer secure-token"}

    def test_add_book(self):
        response = self.client.post("/books", json={"title": "Book1", "author": "Author1"}, headers=self.headers)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json)

    def test_get_books(self):
        response = self.client.get("/books", headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_unauthorized_access(self):
        response = self.client.get("/books")
        self.assertEqual(response.status_code, 401)

if __name__ == "__main__":
    unittest.main()
