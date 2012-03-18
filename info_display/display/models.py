from django.db import models

class SubscriberCount(models.Model):
    total_subscribers = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Subscriber Counts'

    def __unicode__(self):
        return str(self.total_subscribers)


class YesterdaysSignupsCount(models.Model):
    subscribers = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Yesterdays Signup Counts'

    def __unicode__(self):
        return str(self.subscribers)

