from django.db import models

class MainMessage(models.Model):
    message = models.CharField(max_length=120)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.message
