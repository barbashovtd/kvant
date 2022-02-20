from django.db import models
from django.utils.html import mark_safe
from datetime import date

# TODO: перебазировать на User из Django


class City(models.Model):
    name = models.CharField("Город", default="Казань", max_length=32, unique=True)
    region = models.CharField("Регион", default="Татарстан", max_length=64, unique=True)

    def __str__(self) -> str:
        return f"{self.name}  ({self.region})"

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ["name"]


class CustomUserAbstract(models.Model):
    photo = models.ImageField("Фото (файл)", upload_to="photo/", blank=True, null=True)
    name = models.CharField("Имя", max_length=32)
    surname = models.CharField("Фамилия", max_length=64)
    patronymic = models.CharField("Отчество", max_length=64, blank=True, default="")
    birth_date = models.DateField("День рождения", null=True)
    email = models.EmailField("e-mail", blank=True, null=True)
    phone = models.CharField("Телефон", max_length=16, blank=True)
    tg = models.CharField("Телеграм", max_length=33, blank=True)
    inst = models.CharField("Инстаграм", max_length=31, blank=True)
    city = models.ForeignKey(
        City, verbose_name="Город", on_delete=models.DO_NOTHING, blank=True
    )
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    notes = models.TextField("Комментарии", blank=True, null=True)

    class Meta:
        abstract = True

    @property
    def full_name(self) -> str:
        return f"{self.surname} {self.name} {self.patronymic or ''}"

    def calc_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        return (
            age
            if (
                (today.month, today.day) >= (self.birth_date.month, self.birth_date.day)
            )
            else age + 1
        )

    @property
    def photo_preview(self):
        if self.photo:
            return mark_safe(f'<img src="{self.photo.url}" width="256" height="256"/>')
        else:
            return "🤷‍♂️"

    @property
    def qr_preview(self):
        if self.qr:
            return mark_safe(f'<img src="{self.qr.url}" width="256" height="256"/>')
        else:
            return "🤷‍♂️"

    @property
    def is_teacher(self):
        return hasattr(self, "discipline")

    @property
    def is_student(self):
        return hasattr(self, "teacher")

    def save(self, *args, **kwargs) -> None:
        self.age = self.calc_age()
        return super().save(*args, **kwargs)


class Parent(CustomUserAbstract):
    children = models.ManyToManyField(
        "Student",
        verbose_name="Дети",
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.surname} {self.name} {self.patronymic}  ({self.children})"

    class Meta:
        verbose_name = "Родитель"
        verbose_name_plural = "Родители"


class Teacher(CustomUserAbstract):
    section = models.ManyToManyField(
        "Section",
        verbose_name="Секция",
        related_name="teacher_sections",
        blank=True,
    )
    discipline = models.CharField("Предмет", max_length=32)
    is_main = models.BooleanField("Руководитель секции", default=False)
    qr = models.ImageField("QR", upload_to="qr/", blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.surname} {self.name}  ({self.section.name})"

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class Section(models.Model):
    name = models.CharField("Секция", max_length=32)
    teachers = models.ManyToManyField(
        Teacher,
        verbose_name="Преподаватели",
        related_name="section_teachers",
        blank=True,
    )
    students_count = models.PositiveSmallIntegerField("Число учеников", default=0)

    class Meta:
        verbose_name = "Секция"
        verbose_name_plural = "Секции"

    def __str__(self) -> str:
        return f"{self.name}"


class Student(CustomUserAbstract):
    """
    Модель Квантовца

    Parameters
    ----------
    CustomUserAbstract : базовая модель пользователя

    QR-код создаётся только при наличии заполненных имени и фамилии
    При наличии секции и отчества, они также добавляются
    """

    section = models.ForeignKey(
        Section,
        verbose_name="Секция",
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )
    teacher = models.ForeignKey(
        Teacher,
        verbose_name="Преподаватель",
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
    )

    # TODO: если пустой, то создание в post_save (???)
    qr = models.ImageField("QR", upload_to="qr/", blank=True, null=True)

    parents = models.ManyToManyField(
        Parent,
        verbose_name="Родители",
        blank=True,
    )

    class Meta:
        verbose_name = "Квантовец"
        verbose_name_plural = "Квантовцы"

    def __str__(self) -> str:
        section_info = self.section.name if self.section else "🤷‍♂️"
        return f"{self.surname} {self.name}  ({section_info})"
