from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=120, help_text="Username")
    
    def __unicode__(self):
        return unicode(first_name);
    