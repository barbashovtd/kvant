# kvant

Веб-приложение генерации QR-кодов для ЛПШ "КВАНТ" и администрирования.

---

## ToDO

* [ ] VCard для преподов (и студентов?) со всей имеющейся инфой
* [ ] Цвета QR в цвета кванта
* [ ] Добавить фоновое фото преподов/студентов к QR (???)
* [ ] Поздравление с днём рождения
* [ ] ==**Замена ContentFile на ImageFile**==

## Styleguide

### Импорты
* Необходимые импорты Django / DRF (напр. from django.db import models)
* Стандартная библиотека Python (напр. from typing import ...)
* Дополнительные (внешние) модули (напр. import segno)
* Модули, относящиеся к проекту/приложению (напр. from .models import ...)
* Все импорты разделяются пустой строкой
* Импорты модулей проекта/приложения отделяются двойной пустой строкой

Пример:
```python
from django.db.models.signals import pre_save
from django.dispatch import receiver

from typing import Union

import segno, io


from .models import Student, Teacher
```