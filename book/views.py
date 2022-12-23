from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse

def bookview(request):
    book = models.Book.objects.all()
    return render(request, 'book.html', {'book_object': book})


def book_view_detail(request, id):
    book_detail = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html', {'object_detail': book_detail})

def add_book_view(request):
    method = request.method
    if method == 'POST':
        form = forms.ShowForm(request.POST, request.FILES)
        form.save()
        return HttpResponse('<h1>книга успешно добавлена</h1>')

    else:
        form = forms.ShowForm()

    return render(request, 'create_book.html', {'form': form})