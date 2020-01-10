from django.db import models


class Course(models.Model):
    """Курсы"""
    name = models.CharField("Название курса", max_length=200)
    description = models.TextField("Описание курса", blank=True)
    # Потом заменим на ссылку на юзера с ролью "учитель"
    teacher = models.CharField("Учитель", max_length=100, blank=True)

    def __str__(self):
        return self.name


class Theme(models.Model):
    """Тема"""
    name = models.CharField("Название темы", max_length=200)
    description = models.TextField("Описание темы", blank=True)
    course = models.ForeignKey(Course, verbose_name="Курс", on_delete=models.SET_NULL, null=True)
    max_score = models.PositiveSmallIntegerField("Максимальное количество баллов за тему", default=0)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """Урок"""
    name = models.CharField("Название урока", max_length=200, blank=True)
    description = models.TextField("Описание урока", blank=True)
    theme = models.ForeignKey(Theme, verbose_name="Тема", on_delete=models.SET_NULL, null=True)
    order_in_course = models.PositiveSmallIntegerField("Порядок урока в курсе", default=0)

    def __str__(self):
        return self.name


class Unit(models.Model):
    """Юнит урока"""
    UNIT_TYPES = (
        ('at', 'autotest'),
        ('mt', 'manual test'),
        ('vid', 'video'),
        ('text', 'txt'),
    )
    unit_type = models.CharField("Тип юнита", choices=UNIT_TYPES, max_length=25)
    content = models.TextField()
