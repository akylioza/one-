from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookview, name='book'),
    path('book_detail/<int:id>/', views.book_view_detail, name='detail'),
    path('add_book/', views.add_book_view, name='create_book')
]