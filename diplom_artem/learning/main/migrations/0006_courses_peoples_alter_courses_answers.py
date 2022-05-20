# Generated by Django 4.0.4 on 2022-05-15 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_courses_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='peoples',
            field=models.ManyToManyField(blank=True, related_name='courses_for_people', to='main.people'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='answers',
            field=models.ManyToManyField(blank=True, related_name='courses_for_answers', to='main.answer'),
        ),
    ]