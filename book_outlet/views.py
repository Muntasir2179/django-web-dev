from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Book

# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request=request, template_name="book_outlet/index.html", context={"books": books})


def book_details(request, id):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    
    book = get_object_or_404(Book, pk=id)   # this line of code performs the above try except logic
    return render(request=request, 
                  template_name="book_outlet/book_detail.html",
                  context={
                      "title": book.title,
                      "author": book.author,
                      "rating": book.rating,
                      "is_bestselling": book.is_bestselling
                  })