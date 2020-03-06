
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('available-books/', views.AvailableBookListView.as_view(), name='Available Books'),
    path('loaned-books/', views.LoanedBookListView.as_view(), name='Loaned Books'),
    path('late-books/', views.LateBookListView.as_view(), name='Late Books'),
]