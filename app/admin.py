from django.contrib import admin
from .models import Office, Employee
# Register your models here.

@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ["id", "name","location"]
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "email", "gender", "office"]