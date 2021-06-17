# ────────────────────────────────────────────
# file:        urls.py
# project:     api
# Author:      Timur Barbashov        𝑏𝑦 𝑡ℎ𝑒 𝑝𝑒𝑜𝑝𝑙𝑒
# e-mail:      barbashovtd@mail.ru        𝑓𝑜𝑟 𝑡ℎ𝑒 𝑝𝑒𝑜𝑝𝑙𝑒
# June 11th 2021
# ────────────────────────────────────────────
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, TeacherViewSet, SectionViewSet

router = DefaultRouter()
router.register("student", StudentViewSet, "student")
router.register("teacher", TeacherViewSet, "teacher")
router.register("section", SectionViewSet, "section")


urlpatterns = [
    path("", include(router.urls)),
]
