from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from ..forms import LoginForm, SignUpForm

User= get_user_model()
class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('login')
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@test.com',
            password='testpass'
        )

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.assertIsInstance(response.context['form'], LoginForm)

    def test_post_valid_form(self):
        data = {'email': 'testuser@test.com', 'password': 'testpass'}
        response = self.client.post(self.url, data)
        self.assertRedirects(response, '/')
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_post_invalid_form(self):
        data = {'email': 'testuser@test.com', 'password': 'wrongpass'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.assertIsInstance(response.context['form'], LoginForm)
        self.assertContains(response, 'Invalid credentials')

    def test_post_invalid_data(self):
        data = {'invalid_field': 'invalid_value'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.assertIsInstance(response.context['form'], LoginForm)
        self.assertContains(response, 'Error validating the form')


class RegisterUserViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('register')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertIsInstance(response.context['form'], SignUpForm)

    def test_post_valid_form(self):
        data = {
            'email': 'testuser@test.com',
            'password1': 'testpass',
            'password2': 'testpass'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertContains(response, 'User created successfully.')
        self.assertTrue(response.context['success'])

    def test_post_invalid_form(self):
        data = {'email': 'testuser@test.com', 'password1': 'testpass'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertIsInstance(response.context['form'], SignUpForm)
        self.assertContains(response, 'Form is not valid')

    def test_post_invalid_data(self):
        data = {'invalid_field': 'invalid_value'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.assertIsInstance(response.context['form'], SignUpForm)
        self.assertContains(response, 'Form is not valid')
