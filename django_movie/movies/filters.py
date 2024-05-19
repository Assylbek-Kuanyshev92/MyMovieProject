from django_filters import rest_framework as filters

from movies.models import Movie


class MovieFilter(filters.FilterSet):
    class Meta:
        model = Movie
        fields = {
            'title': ['exact', 'contains', 'icontains'],
            'year': ['exact', 'gte', 'lte'],
            'directors': ['exact'],
        }

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        return queryset.distinct()
