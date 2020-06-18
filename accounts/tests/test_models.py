from django.test import TestCase
from accounts.models import AuthorProfile
from django.contrib.auth.models import User

class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username = 'user1',
            email = 'user1@mail.com',
            password = 'SecretKey1'
        )
        self.customer = AuthorProfile.objects.create(
            customer = self.user,
            contact_number = '234534634',
            address = '34 Sdfj st.',
            city = 'Makati'
        )

    def test_authorprofile_created(self):
        self.assertEquals(self.customer.city, 'Makati')