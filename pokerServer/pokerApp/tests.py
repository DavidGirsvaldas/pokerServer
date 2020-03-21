from django.test import TestCase, Client
from django.urls import reverse

class TestPokerAppApi(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse("pokerApp:get_players")

    def test_get_default_game_setup(self):
        result = self.client.get(self.url, {})
        self.assertEqual(200, result.status_code)
        self.assertJSONEqual(result.content, {"name": "test", "stack": 100})
