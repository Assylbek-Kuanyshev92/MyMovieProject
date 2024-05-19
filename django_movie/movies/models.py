from django.db import models

class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")

    def __str__(self):
        return f"{self.name} ({self.pk})"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Actor(models.Model):
    """Актеры и режиссеры"""
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return f"{self.name} ({self.pk})"

    class Meta:
        verbose_name = "Актеры и режиссеры"
        verbose_name_plural = "Актеры и режиссеры"


class Genre(models.Model):
    """Жанры"""
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")

    def __str__(self):
        return f"{self.name} ({self.pk})"

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(models.Model):
    """Фильм"""
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    year = models.IntegerField("Дата выхода")
    directors = models.ManyToManyField(Actor, verbose_name="режиссер", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="актеры", related_name="film_actor")
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title} ({self.pk})"


    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"




