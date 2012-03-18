from django.contrib import admin

from display.models import SubscriberCount


class SubscriberCountAdmin(admin.ModelAdmin):
    pass

admin.site.register(SubscriberCount, SubscriberCountAdmin)
