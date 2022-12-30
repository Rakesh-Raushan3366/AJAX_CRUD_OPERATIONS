from django.shortcuts import render
from django.http import JsonResponse
from app.forms import OfficeForm, EmployeeForm
from django.forms.models import model_to_dict
from app.models import Office, Employee
from django.core import serializers
# Create your views here.

def home(request):
    officeForm = OfficeForm()
    employeeForm = EmployeeForm()
    context = {
        "officeForm": officeForm,
        "employeeForm": employeeForm,
    }
    return render(request, "home.html", context)


def officecurd(request):
    if request.method == "POST":
        print(request.POST)
        officeForm = OfficeForm(request.POST)
        office = officeForm.save()
        return JsonResponse(model_to_dict(office) , safe=True)



def employeecurd(request):
    if request.method == "POST":
        print(request.POST)
        employeeForm = EmployeeForm(request.POST)
        employee = employeeForm.save()
        return JsonResponse(model_to_dict(employee) , safe=True)

def getAllOffices(request):
    offices = Office.objects.all()
    data = serializers.serialize("json", offices)
    return JsonResponse(data , safe=False)



def getAllEmployees(request):
    employees = Employee.objects.all()
    data = serializers.serialize("json", employees)
    return JsonResponse(data , safe=False)