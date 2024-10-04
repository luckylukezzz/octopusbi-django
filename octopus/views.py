from django.shortcuts import render

from .models import School  # Import your models

def dashboard(request):
    schools = School.objects.all()
    context = {
        'schools': schools,
        'table_name': 'Schools'
    }
    return render(request, 'octopus/dashboard.html', context)

def table_view(request, table_name):
    if table_name == 'schools':
        data = School.objects.all()
        for school in data:
            print(f"School ID: {school.id}, School Name: {school.name}")

        headers = ['sch_id', 'school_name'] 
    # Add more elif statements for other tables
    
    context = {
        'data': data,
        'headers': headers,
        'table_name': table_name.capitalize()
    }
    return render(request, 'octopus/table_detail.html', context)