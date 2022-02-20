from django.contrib import admin

from .models import Student, Section, Parent, Teacher, City

# TODO: для пользователей перебазировать на CustomUserAdmin

user_information_fields = (
    "Основная информация",
    {
        "fields": [
            "photo_preview",
            "photo",
            "surname",
            "name",
            "patronymic",
            "birth_date",
            "age",
            "city",
        ],
    },
)
user_contacts_fields = (
    "Контакты",
    {
        "fields": [
            "phone",
            "email",
            "tg",
            "inst",
        ],
    },
)
user_exclude_fields = ("qr",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    def photo_preview(self, obj):
        return obj.photo_preview

    def qr_preview(self, obj):
        return obj.qr_preview

    photo_preview.short_description = "Фото"
    photo_preview.allow_tags = True
    qr_preview.short_description = "QR"
    qr_preview.allow_tags = True

    readonly_fields = (
        "photo_preview",
        "qr_preview",
    )
    exclude = user_exclude_fields
    empty_value_display = "─"

    fieldsets = (
        user_information_fields,
        (
            "Родители",
            {
                "fields": ("parents",),
            },
        ),
        (
            "Квант",
            {
                "fields": (
                    "section",
                    "teacher",
                    "qr_preview",
                ),
            },
        ),
        user_contacts_fields,
        (
            "Дополнительно",
            {
                "fields": ("notes",),
            },
        ),
    )


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    empty_value_display = "─"


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    def photo_preview(self, obj):
        return obj.photo_preview

    photo_preview.short_description = "Фото"
    photo_preview.allow_tags = True

    readonly_fields = ("photo_preview",)
    exclude = user_exclude_fields
    empty_value_display = "─"

    fieldsets = (
        user_information_fields,
        user_contacts_fields,
        (
            "Дети",
            {
                "fields": ("children",),
            },
        ),
        (
            "Дополнительно",
            {
                "fields": ("notes",),
            },
        ),
    )
    exclude = user_exclude_fields


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    def photo_preview(self, obj):
        return obj.photo_preview

    def qr_preview(self, obj):
        return obj.qr_preview

    photo_preview.short_description = "Фото"
    photo_preview.allow_tags = True
    qr_preview.short_description = "QR"
    qr_preview.allow_tags = True

    readonly_fields = (
        "photo_preview",
        "qr_preview",
    )
    exclude = user_exclude_fields
    empty_value_display = "─"

    fieldsets = (
        user_information_fields,
        user_contacts_fields,
        (
            "Квант",
            {
                "fields": (
                    "section",
                    "discipline",
                    "qr_preview",
                ),
            },
        ),
        (
            "Дополнительно",
            {
                "fields": ("notes",),
            },
        ),
    )
    exclude = user_exclude_fields


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    empty_value_display = "─"
    fields = ["__all__"]
