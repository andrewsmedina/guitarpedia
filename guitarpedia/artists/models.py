from django.db import models

class Band(models.Model):
    
    name = models.CharField(max_length=255)
    website = models.URLField(verify_exists=False)
    
    def __unicode__(self):
        return self.name
        
class Guitarrist(models.Model):

    name = models.CharField(max_length=255)
    website = models.URLField(verify_exists=True, null=True)
    biography = models.TextField(null=True)
    date_of_birthday = models.DateField(null=True)
    
    def __unicode__(self):
        return self.name