from django.test import TestCase

from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='yasser', email='yasser@gmail.com', password='1234'
        )
        self.assertEqual(user.username, 'yasser')
        self.assertEqual(user.email, 'yasser@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='superyasser', email='superyasser@gmail.com', password='1234'
        )
        self.assertEqual(user.username, 'superyasser')
        self.assertEqual(user.email, 'superyasser@gmail.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)