from django.db import models



class Fud(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    foto = models.ImageField(upload_to='img/fud/', verbose_name='Картинка')
    price = models.IntegerField(verbose_name='Цена')
    quantity = models.IntegerField(verbose_name='Количество')
    description = models.TextField(verbose_name='Состав')

    def __str__(self):
        return self.title

class A_treat(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    foto = models.ImageField(upload_to='img/fud', verbose_name='Картинка')
    price = models.IntegerField(verbose_name='Цена')
    quantity = models.IntegerField(verbose_name='Количество')
    description = models.TextField(verbose_name='Состав')
    fud = models.ForeignKey(Fud, on_delete=models.CASCADE, related_name="Лакомство")

    def __str__(self):
        return self.title


class Pizza(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    foto = models.ImageField(upload_to='img/fud', verbose_name='Картинка')
    price = models.IntegerField(verbose_name='Цена')
    quantity = models.IntegerField(verbose_name='Количество')
    description = models.TextField(verbose_name='Состав')
    fud = models.ForeignKey(Fud, on_delete=models.CASCADE, related_name='Пицца')

    def __str__(self):
        return self.title

class Drinks(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    foto = models.ImageField(upload_to='img/fud', verbose_name='Картинка')
    price = models.IntegerField(verbose_name='Цена')
    quantity = models.IntegerField(verbose_name='Количество')
    description = models.TextField(verbose_name='Состав')
    fud = models.ForeignKey(Fud, on_delete=models.CASCADE, related_name="Напитки")

    def __str__(self):
        return self.title