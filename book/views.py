from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse
from django.views import generic

class BookView(generic.ListView):
    template_name = 'book.html'
    queryset = models.Book.objects.all()



class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)



class BookCreateView(generic.CreateView):
    template_name = 'create_book.html'
    form_class = forms.ShowForm
    queryset = models.Book.objects.all()
    success_url = 'http://127.0.0.1:8000/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form=form)




class BookUpdateView(generic.UpdateView):
    template_name = 'book_update.html'
    form_class = forms.ShowForm
    success_url = 'http://127.0.0.1:8000/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)

    def form_valid(self, form):
        return super(BookUpdateView, self).form_valid(form=form)



class BookDeleteView(generic.DeleteView):
    template_name = 'confirm_deletion.html'
    success_url = 'http://127.0.0.1:8000/'
    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)


def rating_view(request):
    rating = models.Rating.objects.all()
    return render(request, 'book_detail.html', {'book_rate': rating})


def comment_view(request):
    comment = models.BookComment.objects.all()
    return render(request, 'book_detail.html', {'book_comm': comment})

def expert_recomendation_view(request):
    exp_rec = models.ExpertRecomendation.objects.all()
    return render(request, 'book_detail.html', {'book_recomendation': exp_rec})