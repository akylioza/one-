from django.shortcuts import render, get_object_or_404
from . import models

def bookview(request):
    book = models.Book.objects.all()
    return render(request, 'book.html', {'book_object': book})


def book_view_detail(request, id):
    book_detail = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html', {'object_detail': book_detail})