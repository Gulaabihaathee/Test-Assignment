from django.contrib import admin
from .models import Group, Hero

class Heroes(admin.ModelAdmin):
    list_display = ('hero_name', 'wins_counter', 'defeats_counter', 'is_killed')

admin.site.register(Group)
admin.site.register(Hero, Heroes)