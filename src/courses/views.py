from django.shortcuts import render


# Create your views here.
from courses.models import course

def project_list(request):
    all=course.objects.all()
    return render (request,'project.html',{'data':all})


    