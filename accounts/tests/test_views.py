from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import AuthorProfile
from django.contrib.auth.models import User

class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create 2 users
        cls.users = []
        cls.authors = []
        for i in range(2):
            user = User.objects.create_user(
                username = f'user{i}',
                email = f'user{i}@mail.com',
                password = f'SecretKey{i}'
            )
            cls.users.append(user)


        # create 2 authors
        for i in range(2):
            author = AuthorProfile.objects.create(
                author = cls.users[i],
                contact_number = '234534634',
                address = '34 Sdfj st.'
            )
            cls.authors.append(author)

        # put here those that you will be needing for all your tests and available for each

    def setUp(self):
        self.client = Client()
        self.url = ''

        # put here things that you will need for every test but may change for each test

    # test if login view can be accessed
    def test_login_view_GET(self):
        self.url = reverse('login')
        response = self.client.get(self.url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    # put other tests here

