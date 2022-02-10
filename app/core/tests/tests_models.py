from django.test import TestCase
from django.Contrib.auth import get_user_model

class ModelTests(TestCase):
  def test_create_user_with_email_success(self):
    """Test creating new user with an email is successful"""
    email = 'test@lgmail.com'
    password = 'teste123'
    user = get_user_model().objects.create_user(
      email=email,
      password=password
    )

    self.assertEqual(user.email, email)
    self.assertTrue(user.check_password(password))