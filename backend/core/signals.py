# ────────────────────────────────────────────
# file:        signals.py
# project:     core
# Author:      Timur Barbashov        𝑏𝑦 𝑡ℎ𝑒 𝑝𝑒𝑜𝑝𝑙𝑒
# e-mail:      barbashovtd@mail.ru        𝑓𝑜𝑟 𝑡ℎ𝑒 𝑝𝑒𝑜𝑝𝑙𝑒
# September 1st 2021
# ────────────────────────────────────────────
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.files.base import ContentFile, File
from django.utils.text import slugify

from typing import Union

import segno, io


from .models import Student, Teacher


def get_qr_file(person: Union[Student, Teacher], scale=4) -> bytes:
    data = [person.full_name, person.section.name, person.phone]
    if person.is_teacher:
        data.append(f"Преподаватель: {person.discipline}")
    info = "\n".join(data)
    out = io.BytesIO()
    qr_person = segno.make_qr(info)
    qr_person.save(out, kind="png", scale=scale)
    return out.getvalue()


@receiver(pre_save, sender=Student)
@receiver(pre_save, sender=Teacher)
def qr_create(
    sender: Union[Student, Teacher], instance: Union[Student, Teacher], *args, **kwargs
):
    filename = slugify(instance.full_name, allow_unicode=True)
    qr = ContentFile(content=get_qr_file(instance), name=filename)
    instance.qr = qr
