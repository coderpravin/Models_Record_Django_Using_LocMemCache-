from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)

    def __str__(self):
        return f"The name is {self.name} and the last name is {self.lname}"
