from .models import Employees, EmployeesHours
from rest_framework import serializers


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

class EmployeesHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeesHours
        fields = '__all__'