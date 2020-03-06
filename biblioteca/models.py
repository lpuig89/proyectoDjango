from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

class LibraryUser(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} {self.surname}'

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    library_user = models.ForeignKey(LibraryUser, on_delete=models.CASCADE)
    status = models.BooleanField('Reserve')
    return_date = models.DateField('Return date')

    def __str__(self):
        return self.book.__str__()
