from django.urls import path, include
from rest_framework.routers import DefaultRouter

from DjangoRESTBasic.books_api import views
from DjangoRESTBasic.books_api.views import PublisherViewSet

router = DefaultRouter()
router.register('', PublisherViewSet)

urlpatterns = [
    path('books/', views.ListBooksView.as_view(), name='list-book'),
    path('book/<int:pk>/', views.DetailsBooksView.as_view(), name='details-book'),
    path('publisher_links/', views.PublisherHyperlinkView.as_view(), name='publisher-links'),
    path('publishers/', include(router.urls)),
]