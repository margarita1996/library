from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^library/$' , views.main, name = 'main'),
    url(r'^library/comment/(?P<pk>\d+)/$' , views.comment, name = 'comment'),
    url(r'^library/search_book/$' , views.search_book, name = 'search_book'),
    url(r'^library/search_author/$' , views.search_author, name = 'search_author'),
    url(r'^library/search_date/$' , views.search_date, name = 'search_date'),
    url(r'^library/book_information/(?P<pk>\d+)/$' , views.book_information, name = 'book_information'),
    url(r'^library/registration/$' , views.registration, name = 'library_registration'),

    ]
