from django.urls import path
from . import views

urlpatterns = [
    path('books/search', views.BookSearchView.as_view(), name="search-books")
]