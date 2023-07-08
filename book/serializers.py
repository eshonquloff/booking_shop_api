import PyPDF4
from rest_framework.exceptions import ValidationError
from rest_framework.fields import IntegerField, ImageField
from rest_framework.serializers import ModelSerializer

from book.models import Book


class BookModelSerializer(ModelSerializer):
    page_count = IntegerField(read_only=True, required=False)
    view_count = IntegerField(read_only=True, required=False)
    image = ImageField(required=False)

    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, attrs):
        if attrs.get('book').name.split('.')[-1] != 'pdf':
            raise ValidationError({'message': 'Book is not in pdf format'})
        return attrs


