from django.contrib import admin
from .models import Employees, EmployeesHours

# Register your models here.
admin.site.register(Employees)
admin.site.register(EmployeesHours)