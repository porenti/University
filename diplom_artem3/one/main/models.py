from django.db import models

class Quest(models.Model):
    text = models.TextField(verbose_name = "текст")
    slag = models.CharField(verbose_name = "ссылка", max_length = 40)
    name = models.CharField(verbose_name = "имя", max_length = 1000)

    def __str__(self):
        return self.slag

    class Meta:
        verbose_name = "Веб-квест"
        verbose_name_plural = "Веб-квест"
        ordering = ['name']
