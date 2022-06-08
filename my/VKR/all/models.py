from django.db import models

class Group(models.Model):
    name = models.CharField(verbose_name='Название группы', db_index=True, max_length=10, unique=True)
    rukovoditel = models.OneToOneField('Personal',verbose_name='Куратор', on_delete=models.PROTECT)
    name_napr = models.CharField(verbose_name='Направление', max_length=150)

    def __str__(self):
        return self.name

class Blocked_day(models.Model):
    group = models.ForeignKey("Group", verbose_name="Группа", on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата выходного',auto_now=False, auto_now_add=False)

class Personal(models.Model):
    name = models.CharField(verbose_name='ФИО', db_index=True, max_length=155, unique=True)
    special = models.CharField(verbose_name='Должность', max_length=100)

    def __str__(self):
        return self.name

class Children(models.Model):
    name = models.CharField(verbose_name='ФИО', db_index=True, max_length=155, unique=True)
    date_of_birth = models.DateField(verbose_name='ДР',auto_now=False, auto_now_add=False)
    group = models.ForeignKey('Group', on_delete=models.PROTECT, verbose_name='Группа')

    def __str__(self):
        return self.name

class Closed_day(models.Model):
    persona = models.ForeignKey('Personal',verbose_name='Преподаватель', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='Дата выходного',auto_now=False, auto_now_add=False)

class Room_type(models.Model):
    type_room = models.CharField(verbose_name='Тип аудитории', db_index=True, max_length=100)

    def __str__(self):
        return self.type_room

class Room(models.Model):
    room_number = models.CharField(verbose_name='Аудитория', db_index=True, max_length=10, unique=True)
    type_room = models.ForeignKey('Room_type', verbose_name='Тип Аудитории', on_delete=models.PROTECT)

    def __str__(self):
        return self.room_number

class Work(models.Model): #Нагрузка
    prepod = models.ForeignKey('Personal', verbose_name = "Преподаватель", on_delete=models.PROTECT)
    group = models.ForeignKey('Group', verbose_name = "Группа", on_delete=models.PROTECT)
    subject = models.CharField(verbose_name='Дисциплина', db_index=True, max_length=100)
    hours = models.IntegerField(verbose_name='Часы')
    hours_end = models.IntegerField(verbose_name='Прошло часов')
    room = models.ForeignKey("Room_type", verbose_name = "Тип аудитории", on_delete=models.PROTECT)

class Finished(models.Model): #Выданные часы
    subject = models.ForeignKey("Work", verbose_name = "Дисциплина", on_delete=models.PROTECT)
    hours = models.IntegerField(verbose_name='Часы')

class Raspisanie(models.Model):
    date = models.DateField(verbose_name='Дата',auto_now=False, auto_now_add=False, db_index=True, unique=True)
    json = models.CharField(verbose_name='json', max_length=1000)


class Days(models.Model): #Выданные часы
    date = models.DateField(verbose_name='Рабочий день',auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.date
