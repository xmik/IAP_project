from .models import Employees
from rest_framework import serializers


class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
