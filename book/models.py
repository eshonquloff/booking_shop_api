import PyPDF4
from django.db.models import Model, CharField, PositiveIntegerField, PositiveSmallIntegerField, ForeignKey, CASCADE, \
    FileField, ImageField


class Author(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Genre(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(Model):
    book = FileField(upload_to='books/')
    title = CharField(max_length=255)
    price = PositiveIntegerField(default=0)
    released_date = PositiveSmallIntegerField()
    author = ForeignKey(Author, CASCADE, related_name='books')
    genre = ForeignKey(Genre, CASCADE, related_name='books')
    page_count = PositiveSmallIntegerField()
    view_count = PositiveSmallIntegerField(default=0)
    image = ImageField(upload_to='images/', null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        file = self.book.open()
        reader = PyPDF4.PdfFileReader(file)
        self.page_count = reader.getNumPages()
        return super().save()
