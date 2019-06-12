from django.urls import path, include

urlpatterns = [
    path('', include('branch_offices.urls')),
    path('', include('employees.urls')),
]