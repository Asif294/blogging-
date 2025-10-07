from django.shortcuts import render,redirect
from .import models
def home(request):
    student=models.student.objects.all()
    return render(request,"home.html",{'data':student})

def delete_student(request,roll):
    stu=models.student.objects.get(pk=roll).delete()
    return redirect("homepage")

