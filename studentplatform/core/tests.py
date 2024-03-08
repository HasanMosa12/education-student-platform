from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# test for the parent

class LoginTests(TestCase):


    def test_failed_login_post_request(self):
        response = self.client.post(reverse('login'), {'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertRedirects(response, reverse('login'))

    def test_login_with_invalid_credentials(self):
        response = self.client.post(reverse('login'), {'username': 'nonexistentuser', 'password': 'wrongpassword'})
        self.assertRedirects(response, reverse('login'))

    def test_unauthenticated_access_redirect(self):
        response = self.client.get(reverse('profile'))
        self.assertRedirects(response, reverse('login'))

    def test_logout_functionality(self):
        User.objects.create_user('logoutuser', password='12345')
        self.client.login(username='logoutuser', password='12345')
        response = self.client.get(reverse('logout'))  # Assuming you have a logout view
        self.assertRedirects(response, reverse('login'))