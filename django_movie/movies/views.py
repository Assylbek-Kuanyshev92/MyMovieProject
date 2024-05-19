from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, viewsets, mixins, filters
from rest_framework.filters import OrderingFilter, SearchFilter

from movies.filters import MovieFilter
from movies.models import Movie, Actor, Category, Genre
from movies.serializers import (
    MovieListSerializer,
    MovieDetailSerializer,
    ActorListSerializer,
    ActorDetailSerializer, CategoriesSerializer, GenresSerializer, MovieCreateSerializer,
    ActorCreateSerializer, CategoriesCreateSerializer, GenresCreateSerializer
)


class CategoryListView(generics.ListAPIView):
    """Вывод списка категории"""
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryCreateView(generics.ListCreateAPIView):
    """Добавление категории"""
    queryset = Category.objects.all()
    serializer_class = CategoriesCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


# class CategoryDeleteView(generics.DestroyAPIView):
#     """Удаление категории"""
#     queryset = Category.objects.all()
#     serializer_class = CategoryDeleteSerializer
#     permission_classes = [permissions.IsAuthenticated]


class GenreListView(generics.ListAPIView):
    """Вывод списка жанров"""
    queryset = Genre.objects.all()
    serializer_class = GenresSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['^name', '=description']
    ordering_fields = ['id', 'description']


class GenreCreateView(generics.ListCreateAPIView):
    """Добавление категории"""
    queryset = Genre.objects.all()
    serializer_class = GenresCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class MovieListView(generics.ListAPIView):
    """Вывод списка фильмов"""
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_classes = MovieFilter
    permission_classes = [permissions.IsAuthenticated]

    search_fields = ['^title', '=actors__name']
    ordering_fields = ['title', 'directors__name']


class MovieDetailView(generics.RetrieveAPIView):
    """Вывод фильма"""
    queryset = Movie.objects.filter()
    serializer_class = MovieDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class MovieCreateView(generics.ListCreateAPIView):
    """Добавление фильма"""
    queryset = Movie.objects.all()
    serializer_class = MovieCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class ActorsListView(generics.ListAPIView):
    """Вывод списка актеров"""
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    permission_classes = [permissions.IsAuthenticated]

    search_fields = ['^name', '=id']
    ordering_fields = ['id', 'name', 'description']


class ActorsDetailView(generics.RetrieveAPIView):
    """Вывод актера или режиссера"""
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class ActorCreateView(generics.ListCreateAPIView):
    """Добавление фильма"""
    queryset = Actor.objects.all()
    serializer_class = ActorCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
