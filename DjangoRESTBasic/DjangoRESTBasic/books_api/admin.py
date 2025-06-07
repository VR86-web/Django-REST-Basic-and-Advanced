from django.contrib import admin

from DjangoRESTBasic.books_api.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

