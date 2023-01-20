from django.shortcuts import render

# Create your views here.
from courses.models import course

def create1(request):
    Course=course.objects.all()


    return render(request,{'Course':Course})