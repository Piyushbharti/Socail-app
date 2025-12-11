import django_filters
from .models import Employees

class EmplyeeFilter(django_filters.FilterSet):
    emp_id = django_filters.CharFilter(field_name = 'emp_id', lookup_expr = 'iexact')
    id_start = django_filters.CharFilter(method = "filter_by_id_range", label = "From Emp Id") 
    id_end = django_filters.CharFilter(method = "filter_by_id_range", label = "To Emp Id") 
    class Meta:
        model = Employees
        fields = ['id']
        
    def filter_by_id_range(self, queryset, name, value):
        if name == "id_start":
            return queryset.filter(id__gte = value)
        elif name == "id_end":
            return queryset.filter(id__lte = value)
        else:
            return queryset