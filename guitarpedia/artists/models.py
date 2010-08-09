from django.db import models

class Band(models.Model):
    
    name = models.CharField(max_length=255)
    website = models.URLField(verify_exists=False)
    
    def __unicode__(self):
        return self.name