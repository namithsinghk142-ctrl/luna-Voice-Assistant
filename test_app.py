import unittest
import json
from unittest.mock import patch
from app import app, user_memory

class LunaAITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Reset memory before each test
        user_memory["name"] = None
        user_memory["mood"] = None

    def test_home_page(self):
        """Verify home page loads successfully with 200 status."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Luna AI", response.data)

    def test_greeting_command(self):
        """Verify greeting response."""
        response = self.app.post('/command',
                                 data=json.dumps({"text": "hello"}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("response", data)
        self.assertTrue(len(data["response"]) > 0)

    def test_identity_command(self):
        """Verify identity response."""
        response = self.app.post('/command',
                                 data=json.dumps({"text": "who are you"}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("Luna", data["response"])

    def test_memory_name(self):
        """Verify setting and recalling user name."""
        # Set name
        response = self.app.post('/command',
                                 data=json.dumps({"text": "my name is Namith"}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Namith", response.get_json()["response"])
        self.assertEqual(user_memory["name"], "Namith")

        # Recall name
        response = self.app.post('/command',
                                 data=json.dumps({"text": "what is my name"}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Namith", response.get_json()["response"])

    def test_memory_mood(self):
        """Verify mood detection and memory update."""
        response = self.app.post('/command',
                                 data=json.dumps({"text": "i am sad"}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(user_memory["mood"], "sad")

    def test_calculator(self):
        """Verify calculator arithmetic operations."""
        # Multiplication with x
        response = self.app.post('/command',
                                 data=json.dumps({"text": "what is 45 x 8"}),
                                 content_type='application/json')
        self.assertIn("360", response.get_json()["response"])

        # Addition with word
        response = self.app.post('/command',
                                 data=json.dumps({"text": "12 plus 5"}),
                                 content_type='application/json')
        self.assertIn("17", response.get_json()["response"])

        # Division
        response = self.app.post('/command',
                                 data=json.dumps({"text": "100 divided by 4"}),
                                 content_type='application/json')
        self.assertIn("25", response.get_json()["response"])

    def test_time_and_date(self):
        """Verify time and date inquiries."""
        response = self.app.post('/command',
                                 data=json.dumps({"text": "what time is it"}),
                                 content_type='application/json')
        self.assertIn("The time is", response.get_json()["response"])

        response = self.app.post('/command',
                                 data=json.dumps({"text": "what is the date"}),
                                 content_type='application/json')
        self.assertIn("Today is", response.get_json()["response"])

    def test_recommendations(self):
        """Verify jokes, movies, and games recommendations."""
        # Joke
        response = self.app.post('/command',
                                 data=json.dumps({"text": "tell me a joke"}),
                                 content_type='application/json')
        self.assertIn("response", response.get_json())

        # Movie
        response = self.app.post('/command',
                                 data=json.dumps({"text": "recommend a movie"}),
                                 content_type='application/json')
        self.assertIn("response", response.get_json())

        # Game
        response = self.app.post('/command',
                                 data=json.dumps({"text": "suggest a game"}),
                                 content_type='application/json')
        self.assertIn("response", response.get_json())

    @patch('webbrowser.open')
    def test_search_and_music(self, mock_browser_open):
        """Verify search and YouTube commands trigger browser open."""
        # Search
        response = self.app.post('/command',
                                 data=json.dumps({"text": "search quantum physics"}),
                                 content_type='application/json')
        self.assertIn("Searching for", response.get_json()["response"])
        self.assertTrue(mock_browser_open.called)

        mock_browser_open.reset_mock()

        # Music
        response = self.app.post('/command',
                                 data=json.dumps({"text": "play mockingbird"}),
                                 content_type='application/json')
        self.assertIn("mockingbird", response.get_json()["response"].lower())
        self.assertTrue(mock_browser_open.called)

if __name__ == '__main__':
    unittest.main()
