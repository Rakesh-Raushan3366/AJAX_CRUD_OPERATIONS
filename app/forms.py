from django.forms import ModelForm
from .models import Office, Employee
# Create yours forms here:-

class OfficeForm(ModelForm):
    class Meta:
        model = Office
        fields = "__all__"

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"