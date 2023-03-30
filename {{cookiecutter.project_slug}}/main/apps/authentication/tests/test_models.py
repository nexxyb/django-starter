from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class UserModelTest(TestCase):

    def setUp(self):
        self.user_data = {
            'email': 'test@test.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'bio': 'Test bio',
            'slug': 'john-doe'
        }
        self.user = get_user_model().objects.create_user(**self.user_data)

    def test_create_user(self):
        """
        Test creating a new user with email and password
        """
        self.assertEqual(self.user.email, self.user_data['email'])
        self.assertTrue(self.user.check_password(self.user_data['password']))
        self.assertEqual(str(self.user), 'John Doe')
        self.assertEqual(self.user.get_full_name(), 'John Doe')
        self.assertEqual(self.user.get_short_name(), 'John')

    # def test_user_absolute_url(self):
    #     """
    #     Test getting user absolute url
    #     """
    #     url = reverse("teacher-detail", kwargs={'slug': self.user.slug})
    #     self.assertEqual(self.user.get_absolute_url(), url)

    def test_user_slug(self):
        """
        Test user slug field
        """
        self.assertIsNotNone(self.user.slug)

    def test_save_user(self):
        """
        Test save user method
        """
        self.user.first_name = 'Jane'
        self.user.last_name = 'Doe'
        self.user.save()
        self.assertEqual(self.user.slug, 'jane-doe')

    def test_email_user(self):
        """
        Test email user method
        """
        subject = 'Test subject'
        message = 'Test message'
        from_email = 'test@test.com'
        self.user.email_user(subject, message, from_email)
        self.assertEqual(len(self.mail.outbox), 1)
        self.assertEqual(self.mail.outbox[0].subject, subject)
        self.assertEqual(self.mail.outbox[0].body, message)
        self.assertEqual(self.mail.outbox[0].from_email, from_email)
        self.assertEqual(self.mail.outbox[0].to[0], self.user.email)
