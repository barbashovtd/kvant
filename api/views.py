from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Teacher, Section
from .serializers import TeacherSerializer, StudentSerializer, SectionSerializer


# Проверка по дате в пределах 2 часов
# Если "последнее посещение" было в этих пределах,
#   то считается, что уже был в столовой
#   иначе обновление времени


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer(queryset)


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer(queryset)


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer(queryset)
