from django.contrib import admin

from .models import Author
from .models import Book
from .models import LibraryUser
from .models import Loan
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(LibraryUser)
admin.site.register(Loan)