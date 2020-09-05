from django.urls import path, include
from .views import CreateBook, DetailView, ListBooks, DeleteView, UpdateView, SearchView

app_name = 'books'


urlpatterns = [
    path('create/',CreateBook,name='create'),
    path('list/',ListBooks,name='list'),
    path('detail/<str:pk>/',DetailView,name='detail'),
    path('delete/<str:pk>/',DeleteView,name='delete'),
    path('update/<str:pk>/',UpdateView,name='update'),
    path('search/',SearchView,name='search')


]
