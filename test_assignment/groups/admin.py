from django.contrib import admin
from .heromodel import Hero
from .groupmodel import Group

class Heroes(admin.ModelAdmin):
    list_display = ('hero_name', 'wins_counter', 'defeats_counter', 'is_killed')

admin.site.register(Group)
admin.site.register(Hero, Heroes)