from django.contrib import admin

from display.models import MainMessage


class MainMessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(MainMessage, MainMessageAdmin)
