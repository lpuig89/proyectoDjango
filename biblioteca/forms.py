from django import forms
from django.core.exceptions import ValidationError
from biblioteca.models import Book, LibraryUser


class LoanForm(forms.Form):
    available_books = Book.objects.all().exclude(loan__status=True)
    book = forms.ChoiceField(label='book', choices=available_books)
    available_users = LibraryUser.objects.all()
    user = forms.ChoiceField(label='user', choices=available_users)