from django.contrib import admin

from authorization.models import User
from movies.models import Movie, Actor, Category, Genre

admin.site.register(User)


admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Actor)


