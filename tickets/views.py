from django.shortcuts import render
from api.models import Section, Student, Teacher


def index(request):
    students = Student.objects.all()
    sections = Section.objects.all()
    teachers = Teacher.objects.all()
    context = {"students": students, "sections": sections, "teachers": teachers}
    return render(request, "index.html.j2", context)
