from .models import attendance
import django_filters

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = attendance
        fields = ['employee']