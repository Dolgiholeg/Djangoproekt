from django.contrib import admin
from .models import *


admin.site.register(A_treat)
admin.site.register(Pizza)
admin.site.register(Drinks)
admin.site.register(Today)
admin.site.register(Comment)


class Foto_filmInline(admin.TabularInline):
    fk_name = 'film'
    model = Foto_film


class ActerInline(admin.TabularInline):
    fk_name = 'film_acter'
    model = Acter


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    inlines = [Foto_filmInline, ActerInline,]
