from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms

class Student:
    def __init__(self, name ,grade):
        self.name = name
        self.grade = int(grade)

        if grade >= 60:
            self.g='pass'
        else:
            self.g='fail'

students =[]

class StudentForm(forms.Form):
    name = forms.CharField(label='student name',max_length=100)
    grade = forms.IntegerField(label='student grade')

def index(request):
    return render(request,'p/index.html',{ 'students': students })


def add(request):
    if request.method == "POST":
        name = request.POST['name']
        grade = int(request.POST['grade'])
        student = Student(name,grade)
        students.append(student)

        return HttpResponseRedirect(reverse('p:index'))

    else:
        form = StudentForm()

    return render(request, "p/add.html", {
        "form": form})


# Create your views here.
