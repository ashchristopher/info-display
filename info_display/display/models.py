from django.db import models

class SubscriberCount(models.Model):
    total_subscribers = models.CharField(max_length=120)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Subscriber Counts'

    def __unicode__(self):
        return self.total_subscribers


class YesterdaysSignupsCount(models.Model):
    subscribers = models.CharField(max_length=120)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Yesterdays Signup Counts'

    def __unicode__(self):
        return self.subscribers
