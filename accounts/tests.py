from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import SignUpPageView

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
        
class SignupTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        
    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')
    
    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignUpPageView.as_view().__name__)