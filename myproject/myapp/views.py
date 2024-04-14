from django.shortcuts import render, HttpResponse
from .models import Student

# Create your views here.
def home(request):
    return render(request,"home.html")

def students(request):
    students = Student.objects.all()
    return render(request,"students.html",{"students":students})