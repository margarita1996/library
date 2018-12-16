from django.db import models
from django.utils import timezone


class Author(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField('Имя автора', max_length = 100)
    surname = models.CharField('Фамилия автора', max_length = 100)
    date = models.DateField('Дата рождения автора') #
	
    def __str__(self):
        return self.surname

class Book(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField('Название книги', max_length = 1000)
    date = models.DateField('Дата издания книги в формате гг-мм-дд') #
    author = models.ForeignKey(Author)
    info = models.CharField('Расскажите нам свое мнение о книге', max_length = 1000, null = True, blank = True)
    
    def __str__(self):
        return self.title
    

