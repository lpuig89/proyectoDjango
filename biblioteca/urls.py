
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.BookListView.as_view(), name='book'),
    path('author/', views.AuthorListView.as_view(), name='author'),
    path('libraryuser/', views.LibraryUserListView.as_view(), name='libraryuser'),
    path('available-books/', views.AvailableBookListView.as_view(), name='available-books'),
    path('loaned-books/', views.LoanedBookListView.as_view(), name='loaned-books'),
    path('late-books/', views.LateBookListView.as_view(), name='late-books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('libraryuser/<int:pk>/', views.LibraryUserDetailView.as_view(), name='libraryuser-detail'),
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
    path('libraryuser/create/', views.LibraryUserCreate.as_view(), name='libraryuser_create'),
    path('libraryuser/<int:pk>/update/', views.LibraryUserUpdate.as_view(), name='libraryuser_update'),
    path('libraryuser/<int:pk>/delete/', views.LibraryUserDelete.as_view(), name='libraryuser_delete'),
    path('loan/create/', views.LoanCreate.as_view(), name='loan_create'),
]