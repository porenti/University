from django.db import models

class WebQuest(models.Model):
    name = models.CharField(verbose_name = "Название веб-квеста", max_length = 100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(verbose_name = "Название роли", max_length = 100)
    webquest = models.IntegerField(verbose_name = "Квест id")
    role_id = models.IntegerField(verbose_name = "Роль id")

    def __str__(self):
        return self.name

class Quest_pool(models.Model):
    name = models.CharField(verbose_name = "Название пула", max_length = 100)
    role_id = models.IntegerField(verbose_name = "Роль id")
    quest_pool_id = models.IntegerField(verbose_name = "Пул id")
    slug = models.CharField(verbose_name = "просто ид буквенное", max_length = 40)

    def __str__(self):
        return self.name

class Quest(models.Model):
    name = models.CharField(verbose_name = "Название вопроса", max_length = 100)
    text = models.CharField(verbose_name = "Текст вопроса", max_length = 1000)
    type = models.CharField(verbose_name = "Тип вопроса", max_length = 100)
    answer = models.CharField(verbose_name = "Ответ на вопрос", max_length = 100)
    pool = models.IntegerField(verbose_name = "Пул id")

    def __str__(self):
        return self.name
