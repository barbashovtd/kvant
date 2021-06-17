# ────────────────────────────────────────────
# file:        qr_post_create.py
# project:     signals
# Author:      Timur Barbashov        𝑏𝑦 𝑡ℎ𝑒 𝑝𝑒𝑜𝑝𝑙𝑒
# e-mail:      barbashovtd@mail.ru        𝑓𝑜𝑟 𝑡ℎ𝑒 𝑝𝑒𝑜𝑝𝑙𝑒
# June 17th 2021
# ────────────────────────────────────────────
from django.dispatch import receiver
from django.db.models.signals import post_save
from api.models import Teacher, Student


@receiver(post_save, sender=Student)
def qr_student_create(sender):
    pass


@receiver(post_save, sender=Teacher)
def qr_teacher_create(sender):
    pass
