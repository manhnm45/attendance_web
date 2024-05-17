from .models import employees
from rest_framework import serializers


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = '__all__'