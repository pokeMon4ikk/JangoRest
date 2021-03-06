from rest_framework import serializers
from .models import Author, Biography, Article, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        # exclude = ['uid']
        fields = '__all__'


class BiographyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'


class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ['id']


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookModelSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
