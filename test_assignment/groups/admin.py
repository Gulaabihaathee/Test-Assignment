from django.contrib import admin
from .heromodel import Hero
from .groupmodel import Group
from datetime import datetime
from .pairingmodel import PairingModel



def kill(modeladmin, request, queryset):
    for i in range(len(queryset)):
        queryset[i].kill()

class Heroes(admin.ModelAdmin):
    list_display = ('id','name', 'wins_counter', 'defeats_counter', 'is_killed')
    actions = (kill,)


def make_array(modeladmin, request, queryset):
    for i in range(len(queryset)):
        queryset[i].make_interaction_array()

def make_pairs(modeladmin, request, queryset):
    for i in range(len(queryset)):
        queryset[i].Pairing()


class PairingModelInterface(admin.ModelAdmin):
    list_display = ('group_name', )
    actions = (make_pairs, make_array,)


admin.site.register(Group)
admin.site.register(Hero, Heroes)
admin.site.register(PairingModel, PairingModelInterface)