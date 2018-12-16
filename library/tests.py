from django.test import TestCase
from library.models import Book, Author
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class LibraryTest(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username='rita',email='margarita.kopyova@mail.ru',password='34rita34',first_name='Rita',last_name='Kopyova')
        test_user2 = User.objects.create_user(username='katya',email='margarita.kopyova@mail.ru',password='34rita34',first_name='Katya',last_name='Pushkina')
        test_user1.save()
        test_user2.save()
        Author.objects.create(id = 1, name = 'Александр', surname = 'Пушкин', date = '1860-05-01')
        author_ = Author.objects.get(id = 1)
        Book.objects.create(id = 1, title = 'Капитанская дочка', date = '2018-05-01', author = author_, info = None)
        Book.objects.create(id = 2, title = 'Пиковая дама', date = '2018-05-01', author = author_, info = None)
        Book.objects.create(id = 3, title = 'Руслан и Людмила', date = '2018-05-01', author = author_, info = None)

			
#search_book		
    def test_search_book_redirect_if_not_logged_in(self):
        resp = self.client.get('/library/search_book/')
        self.assertRedirects(resp, '/accounts/login/?next=/library/search_book/')

    def test_search_book_logged_in_correct_get_request(self):
        login = self.client.login(username='rita', password='34rita34')
        resp = self.client.get('/library/search_book/')
        self.assertEqual(str(resp.context['user']), 'rita')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'library/input.html')
		
    def test_search_book_logged_in_correct_post_request(self):
        login = self.client.login(username='rita', password='34rita34')
        resp = self.client.post(reverse('search_book'), {'title': 'Капитанская дочка'})
        self.assertRedirects(resp, '/library/book_information/1/')
		
    def test_search_book_logged_in_incorrect_post_request(self):
        login = self.client.login(username='rita', password='34rita34')
        resp = self.client.post(reverse('search_book'), {'title': 'qwert'})
        self.assertEqual(str(resp.context['user']), 'rita')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'library/exception.html')
		
#search_author		
    def test_search_author_redirect_if_not_logged_in(self):
        resp = self.client.get('/library/search_author/')
        self.assertRedirects(resp, '/accounts/login/?next=/library/search_author/')

    def test_search_author_logged_in_correct_get_request(self):
        login = self.client.login(username='rita', password='34rita34')
        resp = self.client.get('/library/search_author/')
        self.assertEqual(str(resp.context['user']), 'rita')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'library/input.html')
		
    def test_search_author_logged_in_correct_post_request(self):
        login = self.client.login(username='rita', password='34rita34')
        resp = self.client.post(reverse('search_author'), {'surname': 'Пушкин'})
        self.assertEqual(str(resp.context['user']), 'rita')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['books']), 3)
        self.assertTemplateUsed(resp, 'library/book_list.html')
		
    def test_search_author_logged_in_incorrect_post_request(self):
        login = self.client.login(username='rita', password='34rita34')
        resp = self.client.post(reverse('search_author'), {'surname': 'qwert'})
        self.assertEqual(str(resp.context['user']), 'rita')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'library/exception.html')
		
#search_date	
    def test_search_date_redirect_if_not_logged_in(self):
        resp = self.client.get('/library/search_date/')
        self.assertRedirects(resp, '/accounts/login/?next=/library/search_date/')

    def test_search_date_logged_in_correct_get_request(self):
        login = self.client.login(username='rita', password='34rita34')
        resp = self.client.get('/library/search_date/')
        self.assertEqual(str(resp.context['user']), 'rita')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'library/input.html')
		
    def test_search_date_logged_in_correct_post_request(self):
        login = self.client.login(username='rita', password='34rita34')
        resp = self.client.post(reverse('search_date'), {'date': '2018-05-01'})
        self.assertEqual(str(resp.context['user']), 'rita')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['books']), 3)
        self.assertTemplateUsed(resp, 'library/book_list.html')
        		
    def test_search_date_logged_in_incorrect_post_request(self):
        login = self.client.login(username='rita', password='34rita34')
        resp = self.client.post(reverse('search_date'), {'date': '2018-05-02'})
        self.assertEqual(str(resp.context['user']), 'rita')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'library/exception.html')
		
#comment	
    def test_comment_redirect_if_not_logged_in(self):
        resp = self.client.get('/library/comment/1/')
        self.assertRedirects(resp, '/accounts/login/?next=/library/comment/1/')

    def test_comment_logged_in_correct_get_request(self):
        login = self.client.login(username='rita', password='34rita34')
        resp = self.client.get('/library/comment/1/')
        self.assertEqual(str(resp.context['user']), 'rita')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'library/input.html')
		
    def test_comment_logged_in_correct_post_request(self):
        login = self.client.login(username='rita', password='34rita34')
        resp = self.client.post(reverse('comment', kwargs = {'pk':1,}), {'info': 'Супер'})
        self.assertRedirects(resp, '/library/book_information/1/')
		
#book_information	
    def test_book_information_redirect_if_not_logged_in(self):
        resp = self.client.get('/library/book_information/1/')
        self.assertRedirects(resp, '/accounts/login/?next=/library/book_information/1/')

    def test_book_information_logged_in_correct_get_request(self):
        login = self.client.login(username='rita', password='34rita34')
        resp = self.client.get('/library/book_information/1/')
        self.assertEqual(str(resp.context['user']), 'rita')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'library/book_information.html')
		
#main	
    def test_main_correct_get_request(self):
        resp = self.client.get('/library/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'library/main.html')

		

		
		