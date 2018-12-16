from django.shortcuts import render
from django.utils import timezone
from .models import Author, Book
from .forms import NameForm, TitleForm, DateForm, CommentForm, UserForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


def main(request):
    return render(request, 'library/main.html')

@login_required
def book_information(request, pk):
    books = Book.objects.filter(id = int(pk))
    print(pk)
    if len(books) == 0:
        return render(request, 'library/exception.html', context = {'e':1})
    book = books[0]
    if book.info == None:
        flag = 1
    else:
        flag = 0
    return render(request, 'library/book_information.html', context = {'book' : book, 'flag' : flag})

@login_required
def comment(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            new_book = Book.objects.get(id=pk)
            new_book.info = book.info
            new_book.save()
            return HttpResponseRedirect(reverse('book_information', args = (pk,)))
    else:
        form = CommentForm()
        return render(request, 'library/input.html', context = {'form': form})
	    

@login_required
def search_book(request):
    if request.method == "POST":
        form = TitleForm(request.POST)	
        if form.is_valid():
            book = form.save(commit=False)
            books = list(Book.objects.filter(title = book.title))
            if len(books) == 0:
                return render(request, 'library/exception.html', context = {'e':1})
            book = books[0]
            return HttpResponseRedirect(reverse('book_information', args = (book.id,)))
    else:
        form = TitleForm()
        return render(request, 'library/input.html', context = {'form': form})
		
		
@login_required	    
def search_author(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            books = list(Book.objects.filter(author__surname = author.surname))
            if len(books) == 0:
                return render(request, 'library/exception.html', context = {'e':2})
            return render(request, 'library/book_list.html', context = {'books': books})		
    else:
        form = NameForm()
        return render(request, 'library/input.html', context = {'form': form})
		
		
@login_required		
def search_date(request):
    if request.method == "POST":
        form = DateForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            books = list(Book.objects.filter(date = book.date))
            if len(books) == 0:
                return render(request, 'library/exception.html', context = {'e':3})
            return render(request, 'library/book_list.html', context = {'books': books})
    else:
        form = DateForm()
        return render(request, 'library/input.html', context = {'form': form})
			
			
def registration(request):
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user = User.objects.create_user(username=user.username, email=user.email, password=user.password, first_name=user.first_name, last_name=user.last_name)
                user.save()
                return HttpResponseRedirect('/accounts/login/?next=/library/')
            return HttpResponseRedirect('/accounts/login/?next=/library/')
        else:
            form = UserForm()
            return render(request, 'library/registration.html', {'form': form})
