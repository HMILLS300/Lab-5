import unittest
from app import app

class IntegrationTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_calculator(self):
        response = self.app.post("/", data={
            "a": "8",
            "b": "2"
        })

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Sum: 10.0", response.data)
        self.assertIn(b"Difference: 6.0", response.data)
        self.assertIn(b"Product: 16.0", response.data)
        self.assertIn(b"Quotient: 4.0", response.data)

if __name__ == "__main__":
    unittest.main()

