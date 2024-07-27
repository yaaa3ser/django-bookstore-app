from django.test import TestCase
from django.urls import reverse
from .models import Book, Review
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(title='Big Data', author='John Doe', price='29.99')
        cls.user = get_user_model().objects.create_user(username='reviewuser', password='testpass')
        cls.permission = Permission.objects.get(codename='special_status')
        cls.review = Review.objects.create(book=cls.book, review='An excellent book', author=cls.user)
    
    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Big Data')
        self.assertEqual(f'{self.book.author}', 'John Doe')
        self.assertEqual(f'{self.book.price}', '29.99')
    
    def test_book_list_view_for_logged_in_user(self):
        self.client.login(username='reviewuser', password='testpass')
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Big Data')
        self.assertTemplateUsed(response, 'books/book_list.html')
    
    def test_book_list_view_for_logged_out_user(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '%s?next=/books/' % (reverse('account_login')))
        response = self.client.get('%s?next=/books/' % (reverse('account_login')))
        self.assertContains(response, 'Log In')
    
    def test_book_detail_view_with_permission(self):
        self.client.login(username='reviewuser', password='testpass')
        self.user.user_permissions.add(self.permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Big Data')
        self.assertContains(response, 'An excellent book')
        self.assertTemplateUsed(response, 'books/book_detail.html')