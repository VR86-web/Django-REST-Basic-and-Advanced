from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from DjangoRESTBasic.books_api.models import Book
from DjangoRESTBasic.books_api.serializers import BookSerializer


class ListBooksView(APIView):
    def get(self, request):

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailsBooksView(APIView):

    @staticmethod
    def get_obj(pk):
        return get_object_or_404(Book, pk=pk)

    def get(self, request, pk):

        books = self.get_obj(pk)
        serializer = BookSerializer(books)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):

        books = self.get_obj(pk)
        serializer = BookSerializer(books, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):

        book = self.get_obj(pk)
        serializer = BookSerializer(book, data=request.data, partial=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):

        book = self.get_obj(pk)
        book.delete()
        return Response(status=status.HTTP_200_OK)

