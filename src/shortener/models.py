from django.db import models

# Create your models here.

from .utils import code_generator, create_shortcode

class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(KirrURLManager, self).all(*args, **kwargs)


        return qs

class KirrURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True) #everytime model is saved
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    #override save method by writing out the save method (naming )
    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode()
        super(KirrURL, self).save(*args, **kwargs)



    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
