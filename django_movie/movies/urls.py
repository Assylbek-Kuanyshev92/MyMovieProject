from django.urls import path

from movies import views

urlpatterns = [
    path("movie/", views.MovieListView.as_view()),
    path("movie/<int:pk>/", views.MovieDetailView.as_view()),
    path("movie/create/", views.MovieCreateView.as_view()),
    # path("movie/delete/", views.MovieDeleteView.as_view(), name='delete'),
    path("categories/", views.CategoryListView.as_view()),
    path("categories/create/", views.CategoryCreateView.as_view()),
    # path("categories/delete/", views.CategoryDeleteView.as_view(), name='delete'),
    path("genre/", views.GenreListView.as_view()),
    path("genre/create/", views.GenreCreateView.as_view()),
    path("actors/", views.ActorsListView.as_view()),
    path("actors/<int:pk>/", views.ActorsDetailView.as_view()),
    path("actors/create/", views.ActorCreateView.as_view()),
]