from django.shortcuts import render






# Create your views here.
from .models import course

def project_list(request):
    all=course.objects.all()
    return render (request,'project.html',{'data':all})









def post_detail(request,id):
    Post= course.objects.get(id=id)
    return render(request,'single.html',{'data':Post})


    