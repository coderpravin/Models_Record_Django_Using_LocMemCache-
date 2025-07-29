import factory

from .models import Employee

class EmployeeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employee

    name = factory.Faker("first_name")
    lname = factory.Faker("last_name")

