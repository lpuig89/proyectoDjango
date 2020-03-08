from django.db import models
from django.urls import reverse
import datetime 

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.surname}'

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.pk)])
        
class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.pk)])

class LibraryUser(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} {self.surname}'
    def get_absolute_url(self):
        return reverse('libraryuser-detail', args=[str(self.pk)])

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    library_user = models.ForeignKey(LibraryUser, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    return_date = models.DateField(default=datetime.date.today() + datetime.timedelta(weeks=2))
    checkout_date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.book.__str__()

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.book.pk)])