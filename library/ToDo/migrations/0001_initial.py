# Generated by Django 3.2.9 on 2022-04-13 15:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TODO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, verbose_name='Название заметки')),
                ('text', models.TextField(blank=True, verbose_name='Текст заметки')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_active', models.BooleanField(default=True, verbose_name='активна')),
                ('author', models.CharField(blank=True, max_length=256, verbose_name='Автор заметки')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('uid', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, verbose_name='Название проекта')),
                ('description', models.TextField(blank=True, verbose_name='Описание проекта')),
                ('link_to_repo', models.URLField(blank=True, verbose_name='Ссылка на репозиторий проекта')),
                ('devs', models.TextField(blank=True, verbose_name='Разработчики')),
                ('Todo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ToDo.todo', verbose_name='Заметка')),
            ],
        ),
    ]
