# Generated by Django 3.0.2 on 2020-01-10 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название курса')),
                ('description', models.TextField(blank=True, verbose_name='Описание курса')),
                ('teacher', models.CharField(blank=True, max_length=100, verbose_name='Учитель')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_type', models.CharField(choices=[('at', 'autotest'), ('mt', 'manual test'), ('vid', 'video'), ('text', 'txt')], max_length=25, verbose_name='Тип юнита')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название темы')),
                ('description', models.TextField(blank=True, verbose_name='Описание темы')),
                ('max_score', models.PositiveSmallIntegerField(default=0, verbose_name='Максимальное количество баллов за тему')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Course', verbose_name='Курс')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Название урока')),
                ('description', models.TextField(blank=True, verbose_name='Описание урока')),
                ('order_in_course', models.PositiveSmallIntegerField(default=0, verbose_name='Порядок урока в курсе')),
                ('theme', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Theme', verbose_name='Тема')),
            ],
        ),
    ]
