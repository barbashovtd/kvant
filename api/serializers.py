# ────────────────────────────────────────────
# file:        serializers.py
# project:     tickets
# Author:      Timur Barbashov        𝑏𝑦 𝑡ℎ𝑒 𝑝𝑒𝑜𝑝𝑙𝑒
# e-mail:      barbashovtd@mail.ru        𝑓𝑜𝑟 𝑡ℎ𝑒 𝑝𝑒𝑜𝑝𝑙𝑒
# June 4th 2021
# ────────────────────────────────────────────
from rest_framework.serializers import ModelSerializer
from .models import Teacher, Student, Section


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ["__all__"]


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["__all__"]


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = ["__all__"]
