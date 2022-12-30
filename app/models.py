from django.db import models

# Create your models here.

class Office(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Employee(models.Model):
    genders = [
        ("M", "Male"),
        ("F", "Female")
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.CharField(max_length=30, choices=genders)
    office = models.ForeignKey(Office , on_delete=models.CASCADE)
    # active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name
    