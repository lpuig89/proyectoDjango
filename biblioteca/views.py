from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from biblioteca.models import Book, Author, LibraryUser, Loan
from django.views.generic import ListView
from django.utils import timezone
from datetime import date

def index(request):
    context = {
        
    }
    return render(request, 'biblioteca/index.html', context=context)

class AvailableBookListView(ListView):
    model = Book
    def get_queryset(self):
        return Book.objects.filter(loan__status=False)

class LoanedBookListView(ListView):
    model = Book
    def get_queryset(self):
        return Book.objects.filter(loan__status=True)

class LateBookListView(ListView):
    model = Loan
    def get_queryset(self):
        return Loan.objects.filter(return_date__lt=date.today())