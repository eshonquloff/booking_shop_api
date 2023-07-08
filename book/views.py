from random import choice

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from book.filters import BookFilter
from book.models import Book
from book.serializers import BookModelSerializer


class BookModelViewSet(ModelViewSet):
    serializer_class = BookModelSerializer
    parser_classes = FormParser, MultiPartParser
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ('author__name', 'title', 'released_date')
    filterset_class = BookFilter

    def retrieve(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs.get('pk'))
        book.view_count += 1
        book.save()
        serializer = BookModelSerializer(book)
        return Response(serializer.data)

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return Book.objects.all()[:10]
        return super().get_queryset()

    @action(methods=['GET'], detail=False, url_path='top_books/(?P<limit>[^/.]+)')
    def top_books(self, request, limit):
        books = Book.objects.order_by('-view_count')[:int(self.kwargs['limit'])]
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)
