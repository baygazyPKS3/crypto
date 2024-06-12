from django.contrib import admin
from .models import cardAdd, infoAdd
# Register your models here.
@admin.register(cardAdd)
class cardAdmin(admin.ModelAdmin):
    list_display = ['title',]

@admin.register(infoAdd)
class infoAdmin(admin.ModelAdmin):
    list_display = ['title',]