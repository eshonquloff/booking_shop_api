from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe

from book.models import Book, Genre, Author


@admin.register(Book)
class BookModelAdmin(ModelAdmin):
    list_display = ('title', 'headshot_image', 'get_pdf')

    def get_pdf(self, obj: Book):
        return mark_safe(f'<a href="{obj.book.url}" class="button" target="_blank">Show pdf</a>')

    def headshot_image(self, obj: Book):
        if obj.image:
            return mark_safe(
                f'<a href="{obj.image.url}" target="_blank"><img src="{obj.image.url}" width=40 height=40></a>')


@admin.register(Genre)
class GenreModelAdmin(ModelAdmin):
    pass


@admin.register(Author)
class AuthorModelAdmin(ModelAdmin):
    pass
