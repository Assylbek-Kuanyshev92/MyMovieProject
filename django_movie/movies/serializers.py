from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from movies.models import Movie, Actor, Category, Genre


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class CategoriesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        return Category.objects.create(**validated_data)


# class CategoryDeleteSerializer(serializers.Serializer):
#     id = serializers.IntegerField()


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name', 'description')


class GenresCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)


class ActorListSerializer(serializers.ModelSerializer):
    """Вывод списка актеров и режиссеров"""

    class Meta:
        model = Actor
        fields = ("id", "name")


class ActorDetailSerializer(serializers.ModelSerializer):
    """Вывод полного описани актера или режиссера"""

    class Meta:
        model = Actor
        fields = "__all__"


class ActorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)


class MovieListSerializer(serializers.ModelSerializer):
    """Список фильмов"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "category", "year")


class MovieDetailSerializer(serializers.ModelSerializer):
    """Полный фильм"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    directors = ActorListSerializer(read_only=True, many=True)
    actors = ActorListSerializer(read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = Movie
        fields = "__all__"


class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'year']

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


# class MovieDeleteSerializer(serializers.ModelSerializer):
#
#     def destroy(self, validated_data):
#         return Movie.objects.post(id=validated_data['id'])
#
