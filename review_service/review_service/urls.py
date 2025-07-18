# review_service/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("reviews/", views.add_review, name="add-review"),
    path("books/<int:book_id>/reviews/", views.get_book_reviews, name="book-reviews"),
]
