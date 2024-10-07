import unittest
from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_profile(self):
        profile_data = {
            "name": "John Doe",
            "skills": ["Python", "Django"],
            "experience_level": "Intermediate",
            "preferences": {
                "desired_roles": ["Backend Developer"],
                "locations": ["Remote"],
                "job_type": "Full-Time"
            }
        }
        response = self.app.post('/profile', json=profile_data)
        self.assertEqual(response.status_code, 200)

    def test_get_recommendations(self):
        profile_data = {
            "name": "John Doe",
            "skills": ["Python", "Django"],
            "experience_level": "Intermediate",
            "preferences": {
                "desired_roles": ["Backend Developer"],
                "locations": ["Remote"],
                "job_type": "Full-Time"
            }
        }
        response = self.app.post('/recommendations', json=profile_data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
