from django.db import models
from django.contrib import admin
from branch_offices.models import Branch_Offices


# Register your models here.
class Employees(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    branch_office_id = models.ForeignKey(Branch_Offices,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name