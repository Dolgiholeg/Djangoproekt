# Generated by Django 4.2.16 on 2024-10-16 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinoteatr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('foto', models.ImageField(upload_to='img/acter', verbose_name='Картинка')),
                ('role', models.CharField(max_length=20, verbose_name='Роль')),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
                ('foto', models.ImageField(upload_to='img/film', verbose_name='Картинка')),
                ('description', models.TextField(verbose_name='Описание')),
                ('data', models.DateField(verbose_name='Год выхода в прокат')),
                ('country', models.CharField(max_length=20, verbose_name='Страна')),
                ('age', models.IntegerField(verbose_name='Возраст просмотра')),
            ],
        ),
        migrations.CreateModel(
            name='Today',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
                ('foto', models.ImageField(upload_to='img/today', verbose_name='Картинка')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('time', models.TimeField(verbose_name='Время сеансов')),
            ],
        ),
    ]