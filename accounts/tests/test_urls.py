from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import home

class TestUrls(SimpleTestCase):

    def test_home_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, home)

    # put your other tests here