from django.db import models

class Quest(models.Model):
    text = models.CharField(verbose_name = "текст", max_length = 2147483640)
    slag = models.CharField(verbose_name = "ссылка", max_length = 40)
    name = models.CharField(verbose_name = "ссылка", max_length = 1000)

    def __str__(self):
        return self.slag
