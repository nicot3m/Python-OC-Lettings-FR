from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Profile


class ProfilesPageTestCase(TestCase):
    def setUp(self):
        """ Configure the variables for the tests """
        self.good_user = User.objects.create(username="test_user_name")
        self.good_profile = Profile.objects.create(user=self.good_user, favorite_city="test_city")
        self.good_url_index = reverse("profiles:index")
        self.good_url_profile = reverse("profiles:profile",
                                        args=[self.good_profile.user.username])

    def test_happy_profiles_page(self):
        """ Test profiles index page good path """
        response = self.client.get(self.good_url_index)
        self.assertContains(response, "<h1>Profiles</h1>", status_code=200)

    def test_happy_profile_page(self):
        """ Test profiles profile page good path """
        response = self.client.get(self.good_url_profile)
        self.assertContains(response, "<h1>test_user_name</h1>", status_code=200)

    def test_happy_profile_display(self):
        """ Test profiles profile page display """
        response = self.client.get(self.good_url_profile)
        self.assertContains(response, "Favorite city: test_city", status_code=200)


class ProfilesPageEmptyTestCase(TestCase):
    def setUp(self):
        """ Configure the variables for the tests """
        self.good_url_index = reverse("profiles:index")

    def test_happy_profiles_page_with_no_user(self):
        """ Test profiles index page w/o user defined """
        response = self.client.get(self.good_url_index)
        self.assertContains(response, "No profiles are available", status_code=200)
