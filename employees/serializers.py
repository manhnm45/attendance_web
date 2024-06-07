from .models import employees 
from .models import attendance
from rest_framework import serializers


class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = '__all__'


class attendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = attendance
        fields = '__all__'