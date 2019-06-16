from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Employees, EmployeesHours, EmployeesSalaries
from .serializers import EmployeesSerializer, EmployeesHoursSerializer, EmployeesSalariesSerializer
import requests
from pprint import pprint

@csrf_exempt
def invalid_employees_list(request):
    if request.method == 'GET':
        # bad request
        return JsonResponse({'error':'bad request, missing parameter: branchOfficeId'}, status=400)

@csrf_exempt
def employees_list(request, branchOfficeId):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        # TODO: filter employees by branchOfficeId
        employees = Employees.objects.all()
        serializer = EmployeesSerializer(employees, many=True)
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
'''
@csrf_exempt
def employees_hours_list(request):
    if request.method == 'GET':
        employees_hours = EmployeesHours.objects.all()
        serializer = EmployeesHoursSerializer(employees_hours, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        #dla testów potem zmienic porty!! etc
        r = requests.get('http://127.0.0.1:8080/employee_hours/list/')
        #print(r)
        json = r.json()
        #data = JSONParser().parse(r)
        serializer = EmployeesHoursSerializer(data=json)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201, safe=False)
        return JsonResponse(request, status=400)
'''

#synchronization with BO in order to retrieve employee hours
@csrf_exempt
def employees_hours(request):
    url = 'http://127.0.0.1:8080/employee_hours/list/'
    r = requests.get(url,verify=False)
    hours = r.json()
    dict = {}
    for item in hours:
        dict = item

        employees_hours_id = dict.get('employees_hours_id')
        start_date = dict.get('start_date')
        end_date = dict.get('end_date')
        value = dict.get('value')
        employee_id = dict.get('employee_id')

        movie, created = EmployeesHours.objects.get_or_create(
            employees_hours_id=employees_hours_id,
            start_date=start_date,
            end_date=end_date,
            value=value,
            employee_id=employee_id
        )
        if created:
            movie.save()

    #h = EmployeesHours(**dict)
    #h.save()
    #print(request)
    #data = JSONParser().parse(request)
    #serializer = EmployeesHoursSerializer(data=hours)
    #if serializer.is_valid():
        #serializer.save()
        #return JsonResponse(serializer.data, status=201, safe=False)
    #return JsonResponse(request, status=400)
    if request.method == 'GET':
        emp_hours = EmployeesHours.objects.all()
        serializer = EmployeesHoursSerializer(emp_hours, many=True)
        return JsonResponse(serializer.data, safe=False)

#counting salary for each employ and adding to Salaries table
def employees_salaries(request):
    list_of_ids_and_pay = Employees.objects.values_list('employee_id', 'pay')
    list_of_ids_and_values = EmployeesHours.objects.values_list('employee_id', 'value')
    dict_salaries = {}

    for (i,j) in zip(list_of_ids_and_pay, list_of_ids_and_values):
        if i[0] == j[0]:
            salary = i[1] * j[1]
            dict_salaries[i[0]] = salary

    movie, created = EmployeesSalaries.objects.get_or_create(
        employee_salary_id= 1,
        salary= 12312
    )
    if created:
        movie.save()

    #sal = EmployeesHours(**dict_salaries)
    #sal.save()

    if request.method == 'GET':
        emp_sal = EmployeesSalaries.objects.all()
        serializer = EmployeesSalariesSerializer(emp_sal, many=True)
        return JsonResponse(serializer.data, safe=False)
