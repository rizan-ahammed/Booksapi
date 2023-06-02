# from rest_framework import viewsets
from books.models import Category, Book, Favorite
# from booksapi.api.v1.books.serializers import CategorySerializer, BookSerializer, FavoriteSerializer

# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class FavoriteViewSet(viewsets.ModelViewSet):
#     queryset = Favorite.objects.all()
#     serializer_class = FavoriteSerializer

from rest_framework.serializers import ModelSerializer


class BookSerializer(ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"

class FavoriteSerializer(ModelSerializer):
    class Meta:
        model=Favorite
        fields="__all__"
