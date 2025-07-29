from django.shortcuts import render
from .factories import EmployeeFactory
from django.core.cache import cache

# Create your views here.
'''
def generate_person_view(request):

    person = EmployeeFactory.create()
    people = EmployeeFactory.create_batch(250)

    context = {
        "person":person,
        "people" : people
    }

    return render(request, 'employee/employee_list.html', context)
    '''

def generate_person_view(request):
    people = cache.get("employee_list")

    if not people:
        people = EmployeeFactory.build_batch(250)
        cache.set("employee_list", people, timeout=300)

    context = {
        "person":people[0],
        "people" : people
    }
        
    return render(request, 'employee/employee_list.html', context)
