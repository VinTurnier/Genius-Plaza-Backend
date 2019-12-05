# Django Application Imports
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):

    def test_create_user(self):
        ''' test to see if we can create a user'''
        first_name = 'foo'
        last_name = 'bar'
        username ='foobar'
        email = 'foobar@example.com'
        password = 'password'
        user = get_user_model().objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))