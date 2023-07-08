from django_filters import FilterSet, NumberFilter

from book.models import Book


class BookFilter(FilterSet):
    date_from = NumberFilter(field_name='released_date', lookup_expr='gte')
    date_to = NumberFilter(field_name='released_date', lookup_expr='lte')

    class Meta:
        model = Book
        fields = ('genre__name', 'price', 'author__name', 'date_from', 'date_to')
