from django.db import models



# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    profile = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='agent_images', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name