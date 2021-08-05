from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


class LettingsPageTestCase(TestCase):
    def setUp(self):
        """ Configure the variables for the tests """
        self.good_address = Address.objects.create(number=101, street="test_street",
                                                   city="test_city", state="test_state",
                                                   zip_code=55555, country_iso_code="THA")
        self.good_letting = Letting.objects.create(title="test_letting", address=self.good_address)
        self.good_url_index = reverse("lettings:index")
        self.good_url_letting = reverse("lettings:letting", args=[self.good_address.id])

    def test_happy_lettings_page(self):
        """ Test lettings index page good path """
        response = self.client.get(self.good_url_index)
        self.assertContains(response, "<h1>Lettings</h1>", status_code=200)

    def test_happy_letting_page(self):
        """ Test lettings letting page good path """
        response = self.client.get(self.good_url_letting)
        self.assertContains(response, "<h1>test_letting</h1>", status_code=200)

    def test_happy_lettings_display(self):
        """
        Test lettings index page good display
        Count the number of hyperlinks: 1 for letting, 1 for home and 1 for profiles

        """
        response = self.client.get(self.good_url_index)
        self.assertContains(response, "href", count=3, status_code=200)

    def test_happy_letting_display(self):
        """ Test lettings letting page display """
        response = self.client.get(self.good_url_letting)
        self.assertContains(response, "101 test_street", status_code=200)
        self.assertContains(response, "test_city, test_state 55555", status_code=200)
        self.assertContains(response, "THA", status_code=200)


class LettingsPageEmptyTestCase(TestCase):
    def setUp(self):
        """ Configure the variables for the tests """
        self.good_url_index = reverse("lettings:index")

    def test_happy_profiles_page_with_no_letting(self):
        """ Test profiles index page w/o user defined """
        response = self.client.get(self.good_url_index)
        self.assertContains(response, "No lettings are available", status_code=200)
