from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Employees, EmployeesHours
from .serializers import EmployeesSerializer, EmployeesHoursSerializer
import requests
from pprint import pprint

@csrf_exempt
def employees_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        employees_hours = Employees.objects.all()
        serializer = EmployeesSerializer(employees_hours, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(request, status=400)

@csrf_exempt
def employees_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        branch_offices = Employees.objects.get(pk=pk)
    except Employees.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EmployeesSerializer(branch_offices)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EmployeesSerializer(branch_offices, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        branch_offices.delete()
        return HttpResponse(status=204)

@csrf_exempt
def employees_hours_list(request):
    if request.method == 'GET':
        employees_hours = EmployeesHours.objects.all()
        serializer = EmployeesHoursSerializer(employees_hours, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        #dla testów potem zmienic porty!! etc
        r = requests.get('http://127.0.0.1:8000/employee_hours/list/')
        #print(r)
        #json = r.json()
        data = JSONParser().parse(r)
        serializer = EmployeesHoursSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(request, status=400)