from django.shortcuts import render
from .import models
def home(request):
    student=models.student.objects.all()
    return render(request,"home.html",{'data':student})
