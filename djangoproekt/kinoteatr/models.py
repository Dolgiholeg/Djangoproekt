from django.db import models


class A_treat(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    foto = models.ImageField(upload_to='img/fud', verbose_name='Картинка')
    price = models.IntegerField(verbose_name='Цена')
    quantity = models.IntegerField(verbose_name='Количество')
    description = models.TextField(verbose_name='Состав')

    def __str__(self):
        return self.title


class Pizza(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    foto = models.ImageField(upload_to='img/fud', verbose_name='Картинка')
    price = models.IntegerField(verbose_name='Цена')
    quantity = models.IntegerField(verbose_name='Количество')
    description = models.TextField(verbose_name='Состав')

    def __str__(self):
        return self.title


class Drinks(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    foto = models.ImageField(upload_to='img/fud', verbose_name='Картинка')
    price = models.IntegerField(verbose_name='Цена')
    quantity = models.IntegerField(verbose_name='Количество')
    description = models.TextField(verbose_name='Состав')

    def __str__(self):
        return self.title


class Today(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    foto = models.ImageField(upload_to='img/today', verbose_name='Картинка')
    price = models.IntegerField(verbose_name='Цена')
    time = models.CharField(max_length=20, verbose_name='Время сеансов')

    def __str__(self):
        return self.title


class Film(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    year = models.IntegerField(null=True, verbose_name='Год выхода в прокат')
    country = models.CharField(max_length=20, verbose_name='Страна')
    age = models.CharField(max_length=3, verbose_name='Возраст просмотра')

    def __str__(self):
        return self.title


class Acter(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    foto = models.ImageField(upload_to='img/acter', verbose_name='Картинка')
    role = models.CharField(max_length=20, verbose_name='Роль')
    film_acter = models.ForeignKey(Film, on_delete=models.CASCADE, null=True, related_name='acter')

    def __str__(self):
        return self.name


class Foto_film(models.Model):
    foto = models.ImageField(upload_to='img/foto_film', verbose_name='Картинка')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='foto_film')


class Comment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
