from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("<slug:slug>", view=views.book_details, name="book-detail"),
]
