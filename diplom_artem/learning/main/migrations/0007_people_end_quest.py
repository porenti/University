# Generated by Django 4.0.4 on 2022-05-15 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_courses_peoples_alter_courses_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='end_quest',
            field=models.ManyToManyField(blank=True, related_name='end_quest_user', to='main.answer'),
        ),
    ]