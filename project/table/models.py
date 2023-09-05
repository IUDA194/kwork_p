from django.db import models
from django.utils import timezone
from datetime import datetime

class vacancies(models.Model):
    id_of_vacancie = models.TextField(default=None)
    category = models.TextField(default="Не указанно")
    contacts = models.TextField(default="Не указанно")
    zp = models.TextField(default="По договорённости")
    date = models.DateField(default=timezone.now)
    source = models.TextField(default="Ручной ввод")
    name = models.TextField(default=None)
    description = models.TextField(default=None)
    status = models.TextField(default=None)
    rubr_atrub = models.TextField(default=None)
    conter_name = models.TextField(default=None)
    file_or_link = models.TextField(default=None)
    prefix = models.TextField(default=None)

class job_seekers(models.Model):
    id_of_seekers = models.TextField(default=None)
    fio = models.TextField(default="Вася Пупкин Анатольевич")
    phone = models.TextField(default="+номер не ввёл уёбок")
    date = models.DateField(default=timezone.now)
    email = models.TextField(default="shit@govno.com")
