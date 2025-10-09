from django.shortcuts import render,redirect,get_object_or_404
from .import models
def home(request):
    student=models.student.objects.all()
    return render(request,"home.html",{'data':student})

def delete_student(request,roll):
    stu=models.student.objects.get(pk=roll).delete()
    return redirect("homepage")

def edit_student(request, roll):
    stu=models.student.objects.get(pk=roll)
    if request.method == "POST":
        stu.name = request.POST.get("name")
        stu.father_name = request.POST.get("father_name")
        stu.address = request.POST.get("address")
        stu.save()
        return redirect("homepage")
    return render(request, 'edit.html', {'student':stu})


