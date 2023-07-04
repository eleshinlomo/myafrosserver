from django.db import models

# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=200, blank=False, null=False)
    password = models.CharField(max_length=200, blank=False, null=False)
    email = models.CharField(max_length=200, blank=False, null=False)
    

    class Meta:
        verbose_name_plural = 'Members'
    
    
    def __str__(self):
        return self.username
    
    
