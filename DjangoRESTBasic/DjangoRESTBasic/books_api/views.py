from django.shortcuts import render, get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from DjangoRESTBasic.books_api.models import Book, Publisher
from DjangoRESTBasic.books_api.serializers import BookSerializer, PublisherHyperlinkSerializer, PublisherSerializer, \
    BookSimpleSerializer


class ListBooksView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSimpleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class DetailsBooksView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSimpleSerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherHyperlinkView(ListAPIView):

    queryset = Publisher.objects.all()
    serializer_class = PublisherHyperlinkSerializer
