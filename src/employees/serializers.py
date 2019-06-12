from .models import Employees, EmployeesHours, EmployeesSalaries
from rest_framework import serializers


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

class EmployeesHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeesHours
        fields = '__all__'

class EmployeesSalariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeesSalaries
        fields = '__all__'