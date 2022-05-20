from django.db import models
from django.urls import reverse


class people(models.Model):
    #id - standart
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    end_quest = models.ManyToManyField("main.answer",
                                     blank=True,
                                     symmetrical=False,
                                     related_name="end_quest_user")

    def __str__(self):
        return self.name


class courses(models.Model):
    course_name = models.CharField(max_length=255, verbose_name="Название курса")
    author = models.CharField(max_length=255, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание")
    peoples = models.ManyToManyField("main.people",
                                     blank=True,
                                     symmetrical=False,
                                     related_name="courses_for_people")


    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return reverse('course_info', kwargs={'course_id': self.id})

    class Meta:
        verbose_name = "Курсы"
        verbose_name_plural = "Курсы"

class answer(models.Model):
    name_answer = models.CharField(max_length=255, verbose_name="Название задания")
    answer = models.TextField(verbose_name="Текст задания")
    key = models.CharField(max_length=255, verbose_name="Ответ")
    course = models.ManyToManyField("main.courses",
                                     blank=True,
                                     symmetrical=False,
                                     related_name="answers_for_courses")

    class Meta:
        verbose_name = "Задания"
        verbose_name_plural = "Задания"

    def __str__(self):
        return self.name_answer
