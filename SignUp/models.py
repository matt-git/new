from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class SignUp(models.Model):
    trend = models.CharField(max_length=120, null=True, blank=True, default="Hello")
    #last_name = models.CharField(max_length=120, null=True, blank=True)
    #email = models.EmailField(null=False, blank=False)
    #This means there needs to be a required value when someone submits a form
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    #When its created, make a time stamp, when its updated or change, make not of it(false)
    #Indicates when its first created
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    #Indicates current date time field
    
    def __unicode__(self):
        return smart_unicode(self.trend)
    