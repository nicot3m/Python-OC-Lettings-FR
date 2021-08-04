from django.test import TestCase
from django.urls import reverse


class HomePageTestCase(TestCase):
    def setUp(self):
        self.wrong_url = "/wrong_path"
        self.good_url = reverse("index")

    def test_sad_home_page(self):
        """ Test home page wrong path"""
        response = self.client.get(self.wrong_url)
        assert response.status_code == 404

    def test_happy_home_page(self):
        """ Test home page good path"""
        response = self.client.get(self.good_url)
        self.assertContains(response, "<h1>Welcome to Holiday Homes</h1>", status_code=200)
