from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client

class YourTestClass(TestCase):
    def test_invalid_signup_student_form(self):
        data = {'username': ''}  # Missing required field
        response = self.client.post(reverse('signup_student'), data)
        self.assertEqual(response.status_code, 400)  # Use 400 for a bad request
        self.assertTrue(response.context['form'].has_errors())
        self.assertEqual(response.context['form']['username'].errors, ['This field is required.'])

    def test_successful_student_signup(self):
        self.assertEqual(User.objects.count(), 0)
        data = {
            'username': 'newstudent',
            'email': 'student@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        response = self.client.post(reverse('signup_student'), data)
        self.assertEqual(User.objects.count(), 1)
        self.assertRedirects(response, expected_url=reverse('some_next_page'))  # Adjust the expected URL accordingly

    def test_signup_with_incomplete_data(self):
        data = {'username': 'newstudent'}  # Missing 'email' and 'password'
        response = self.client.post(reverse('signup_student'), data)
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(response.status_code, 400)  # Use 400 for a bad request
        self.assertTrue('form' in response.context)
        self.assertFalse(response.context['form'].is_valid())

    def test_signup_with_duplicate_username(self):
        User.objects.create_user(username='existinguser', email='existing@example.com', password='test123')
        data = {
            'username': 'existinguser',
            'email': 'newemail@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        }
        response = self.client.post(reverse('signup_student'), data)
        self.assertEqual(User.objects.count(), 1)  # No new user should be added
        self.assertTrue(response.context['form'].errors)  # Check for errors in the form
