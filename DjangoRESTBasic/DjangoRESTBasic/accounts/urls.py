from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from DjangoRESTBasic.accounts import views

urlpatterns = [
    path('login/', ObtainAuthToken.as_view(), name='login'),
    path('register/', views.RegisterAPIView.as_view(), name='register'),
]