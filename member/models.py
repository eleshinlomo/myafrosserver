from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.hashers import make_password



# Create your models here.
class Member(models.Model):
    
    username = models.CharField(max_length=200, blank=False, null=False)
    password = models.CharField(max_length=200, blank=False, null=False)
    email = models.CharField(max_length=200, blank=False, null=False)
    token = models.IntegerField(default=0, editable=False)
    has_token = models.BooleanField(default=False)





    

    class Meta:
        verbose_name_plural = 'Members'
    
    
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Member, self).save(*args, **kwargs)



        class MemberManager(BaseUserManager):
            def create_user(self, email, username, password=None):
                if not email:
                    raise ValueError("The Email field must be set")
                email = self.normalize_email(email)
                user = self.model(email=email, username=username)
                user.set_password(password)
                user.save(using=self._db)
                return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email=email, username=username, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


    
    
