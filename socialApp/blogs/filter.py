import django_filters
from .models import Blog

class BlogFilter(django_filters.FilterSet):
    id = django_filters.CharFilter(field_name = 'id', lookup_expr = 'iexact')
    
    class Meta:
        model = Blog
        fields = ['id']