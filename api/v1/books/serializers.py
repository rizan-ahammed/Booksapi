from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from books.models import Category, Book


class BookSerializer(ModelSerializer):
    
    categories=serializers.SerializerMethodField()
    class Meta:
        model=Book
        fields="__all__"

    def get_categories(self, instance):
        return [category.name for category in instance.categories.all()]

