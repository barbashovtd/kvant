# ────────────────────────────────────────────
# file:        models.py
# project:     tickets
# Author:      Timur Barbashov        𝑏𝑦 𝑡ℎ𝑒 𝑝𝑒𝑜𝑝𝑙𝑒
# e-mail:      barbashovtd@mail.ru        𝑓𝑜𝑟 𝑡ℎ𝑒 𝑝𝑒𝑜𝑝𝑙𝑒
# June 15th 2021
# ────────────────────────────────────────────
from django.db.models import Model, ForeignKey
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import (
    CharField,
    DateField,
    DateTimeField,
    IntegerField,
    TextField,
)
from datetime import datetime

from django.forms import ImageField

# Students -> Sections -> Teachers


class Section(Model):
    name = CharField("Название", max_length=64)
    students_count = IntegerField(
        "Количество учеников", default=0, blank=True, null=True
    )
    duties_count = IntegerField("Количество дежурств", default=0, blank=True, null=True)
    notes = TextField("Заметки", null=True, blank=True)

    class Meta:
        verbose_name = "Секция"
        verbose_name_plural = "Секции"

    def __str__(self) -> str:
        return f"{self.name}"


class Teacher(Model):
    second_name = CharField("Фамилия", max_length=64)
    first_name = CharField("Имя", max_length=64)
    patronymic = CharField("Отчество", max_length=64, blank=True)
    qr_code = ImageField(allow_empty_file=True)
    last_ate = DateTimeField(
        "Последнее посещение столовой",
        default=datetime(1970, 1, 1),
    )
    residence = CharField("Искать в", max_length=64, blank=True)
    section = ForeignKey(
        Section,
        verbose_name="Секция",
        on_delete=DO_NOTHING,
        blank=True,
        null=True,
        default=None,
    )
    # TODO переписать на множественный выбор
    subjects = CharField("Предмет/-ы", max_length=256, blank=True)
    notes = TextField("Заметки", null=True, blank=True)

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

    def __str__(self) -> str:
        section = f" ({self.section})" if self.section else ""
        patronymic = f" {self.patronymic}" if self.patronymic else ""
        return f"{self.second_name} {self.first_name}{patronymic}{section}"


class Student(Model):
    second_name = CharField("Фамилия", max_length=64)
    first_name = CharField("Имя", max_length=64)
    patronymic = CharField("Отчество", max_length=64, blank=True)
    qr_code = ImageField(allow_empty_file=True)
    age = IntegerField("Возраст", blank=True, null=True)
    last_ate = DateTimeField(
        "Последнее посещение столовой",
        default=datetime(1970, 1, 1),
    )
    residence = CharField("Искать в", max_length=64, blank=True)
    school = CharField("Школа", max_length=128, blank=True)
    birthday = DateField("День рождения", blank=True, null=True)
    section = ForeignKey(
        Section,
        on_delete=DO_NOTHING,
        blank=True,
        null=True,
        default=None,
    )
    notes = TextField("Заметки", null=True, blank=True)

    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"

    def __str__(self) -> str:
        patronymic = f" {self.patronymic}" if self.patronymic else ""
        return f"{self.second_name} {self.first_name}{patronymic}"
