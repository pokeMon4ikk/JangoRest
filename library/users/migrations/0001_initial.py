# Generated by Django 3.2.9 on 2022-04-13 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=256, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=256, verbose_name='Фамилия')),
                ('birthday_year', models.PositiveIntegerField()),
                ('gender', models.CharField(blank=True, choices=[('M', 'Мужчина'), ('W', 'Женщина'), ('X', 'Небинарный')], max_length=1, verbose_name='пол')),
                ('age', models.PositiveIntegerField(verbose_name='Возраст')),
            ],
        ),
        migrations.CreateModel(
            name='UserMoreInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.CharField(blank=True, choices=[('Спорт', 'Спорт'), ('Искусство', 'Искусство'), ('Музыка', 'Музыка'), ('Танцы', 'Танцы'), ('Коллекционирование', 'Коллекционирование'), ('IT', 'IT'), ('Книги', 'Книги'), ('Вышивание', 'Вышивание'), ('Саморазвитие', 'Саморазвитие'), ('Путешествие', 'Путешествие'), ('Другое', 'Другое')], max_length=128, verbose_name='Хобби')),
                ('spouse_name', models.CharField(blank=True, max_length=128, verbose_name='Имя супруга')),
                ('work', models.CharField(blank=True, max_length=128, verbose_name='Работа')),
                ('work_description', models.TextField(blank=True, verbose_name='Описание работы')),
                ('salary_level', models.CharField(blank=True, choices=[('Low', '10-50 тысяч'), ('Average', '50-120 тысяч'), ('Big', '120+ тысяч')], max_length=128, verbose_name='Уровень зарплаты')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='Пользователь')),
            ],
        ),
    ]
