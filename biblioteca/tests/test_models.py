from django.test import TestCase
from biblioteca.models import Author, Book, LibraryUser

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(name='Peter', surname='Parker')

    def test_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')


    def test_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_surname_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('surname').verbose_name
        self.assertEquals(field_label, 'surname')


    def test_surname_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('surname').max_length
        self.assertEquals(max_length, 100)

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        self.assertEquals(author.get_absolute_url(), '/biblioteca/author/1/')

class LibraryUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        LibraryUser.objects.create(name='Peter', surname='Parker')

    def test_name_label(self):
        libraryuser = LibraryUser.objects.get(id=1)
        field_label = libraryuser._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')


    def test_name_max_length(self):
        libraryuser = LibraryUser.objects.get(id=1)
        max_length = libraryuser._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_surname_label(self):
        libraryuser = LibraryUser.objects.get(id=1)
        field_label = libraryuser._meta.get_field('surname').verbose_name
        self.assertEquals(field_label, 'surname')


    def test_surname_max_length(self):
        libraryuser = LibraryUser.objects.get(id=1)
        max_length = libraryuser._meta.get_field('surname').max_length
        self.assertEquals(max_length, 100)

    def test_get_absolute_url(self):
        libraryuser = LibraryUser.objects.get(id=1)
        self.assertEquals(libraryuser.get_absolute_url(), '/biblioteca/libraryuser/1/')

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title ='Harryy Potter')

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')


    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        self.assertEquals(book.get_absolute_url(), '/biblioteca/book/1/')