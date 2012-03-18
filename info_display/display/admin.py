from django.contrib import admin

from display.models import SubscriberCount, YesterdaysSignupsCount


class SubscriberCountAdmin(admin.ModelAdmin):
    list_display = ('total_subscribers', 'date_added', )


class YesterdaysSignupsCountAdmin(admin.ModelAdmin):
    list_display = ('subscribers', 'date_added', )

admin.site.register(SubscriberCount, SubscriberCountAdmin)
admin.site.register(YesterdaysSignupsCount, YesterdaysSignupsCountAdmin)
