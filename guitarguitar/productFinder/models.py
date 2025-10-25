from django.db import models

# Create your models here.
class Product(models.Model):
    artist = models.CharField()
    amp = models.CharField()
    amp_url = models.URLField()
    guitar = models.CharField()
    guitar_url = models.URLField()
    pedal = models.CharField()
    pedal_url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title