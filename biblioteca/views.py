from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from biblioteca.models import Book, Author, LibraryUser, Loan
from django.views import generic
from django.utils import timezone
from datetime import date
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import LoanForm

def index(request):
    context = {
        
    }
    return render(request, 'biblioteca/index.html', context=context)

class BookListView(generic.ListView):

        model = Book

class AuthorListView(generic.ListView):

        model = Author

class LibraryUserListView(generic.ListView):

        model = LibraryUser

class AvailableBookListView(generic.ListView):

    def get_queryset(self):
        return Book.objects.all().exclude(loan__status=True)

class LoanedBookListView(generic.ListView):

    def get_queryset(self):
        return Book.objects.filter(loan__status=True)

class LateBookListView(generic.ListView):

    def get_queryset(self):
        return Loan.objects.filter(return_date__lt=date.today(), status=True)

class BookDetailView(generic.DetailView):

    model = Book

class AuthorDetailView(generic.DetailView):

    model = Author

class LibraryUserDetailView(generic.DetailView):

    model = LibraryUser

class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'

class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')

class LibraryUserCreate(CreateView):
    model = LibraryUser
    fields = '__all__'

class LibraryUserUpdate(UpdateView):
    model = LibraryUser
    fields = '__all__'

class LibraryUserDelete(DeleteView):
    model = LibraryUser
    success_url = reverse_lazy('libraryuser')

def LoanCreate(request):
    context = {
        'form': LoanForm(),
    }
    return render(request, 'biblioteca/loan_form.html', context)