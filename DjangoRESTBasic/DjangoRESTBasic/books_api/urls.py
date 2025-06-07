from django.urls import path

from DjangoRESTBasic.books_api import views

urlpatterns = [
    path('books/', views.ListBooksView.as_view(), name='list-book'),
    path('book/<int:pk>/', views.DetailsBooksView.as_view(), name='details-book'),
]