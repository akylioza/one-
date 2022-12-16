from django.shortcuts import render
from . import models

def bookview(request):
    book = models.Book.objects.all()
    return render(request, 'book.html', {'book_object': book})
