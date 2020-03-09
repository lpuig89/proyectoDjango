from django import forms
from django.forms import ModelForm
from django.forms import modelformset_factory
from biblioteca.models import Loan, Book


class LoanCreateForm(ModelForm): 
    class Meta:
        model = Loan
        fields = ['book', 'library_user']
        
    def __init__(self, *args, **kwargs):
        super(LoanCreateForm, self).__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.all().exclude(loan__status=True)