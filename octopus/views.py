from django.shortcuts import render
from .models import School, Answer, Assess, Class, Award, Student, Subject

def dashboard(request):
    context = {
        'schools': School.objects.all(),
        'answers': Answer.objects.all(),
        'assessments': Assess.objects.all(),
        'classes': Class.objects.all(),
        'awards': Award.objects.all(),
        'students': Student.objects.all(),
        'subjects': Subject.objects.all(),
    }
    return render(request, 'dashboard.html', context)