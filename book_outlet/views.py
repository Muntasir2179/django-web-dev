from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Avg, Max, Min

from .models import Book

# Create your views here.

def index(request):
    # if we want to order the data in some way
    # books = Book.objects.all().order_by("rating")   # Ascending order
    # books = Book.objects.all().order_by("-rating")   # Descending order
    books = Book.objects.all()
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(request=request,
                  template_name="book_outlet/index.html",
                  context={
                      "books": books,
                      "total_number_of_books": num_books,
                      "average_rating": avg_rating
                  })


def book_details(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    
    book = get_object_or_404(Book, slug=slug)   # this line of code performs the above try except logic
    return render(request=request, 
                  template_name="book_outlet/book_detail.html",
                  context={
                      "title": book.title,
                      "author": book.author,
                      "rating": book.rating,
                      "is_bestselling": book.is_bestselling
                  })