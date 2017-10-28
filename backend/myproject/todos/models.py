from django.db import models
# Leverage Django's built-in User models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

<<<<<<< HEAD
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    campaign = models.ForeignKey(Campaigns, null=True, blank=True)
=======
class NPOProfile(models.Model):   
    username = models.CharField(max_length = 128)
    password = models.CharField(max_length = 128)
    name = models.CharField(max_length = 128)
    description = models.TextField()
>>>>>>> 5d730f1e37474c9184cdb2b6bdf2a53a9a674098

    def __str__(self):
          return "%s's profile" % self.user

<<<<<<< HEAD
def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)


class NPOProfile(models.Model):
    npo_user = models.OneToOneField(User)
   	campaign = models.ForeignKey(Campaigns, null=True, blank=True)

    def __str__(self):
          return "%s's profile" % self.user
=======
class Campaigns(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    npo = models.ForeignKey(NPOProfile, null=True, blank=True)
    actions = models.CharField(max_length=128, null=False, blank=False)
    date_created = models.DateField(null=True, blank=True)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description


class UserProfile(models.Model):  
    first_name = models.CharField(max_length = 128)
    last_name = models.CharField(max_length = 128)
    username = models.CharField(max_length = 128)
    password = models.CharField(max_length = 128)
    email = models.CharField(max_length = 128)

    def __str__(self):  
        return "%s's profile" % self.user  
        
    
    
          
>>>>>>> 5d730f1e37474c9184cdb2b6bdf2a53a9a674098

def create_user_profile(sender, instance, created, **kwargs):  
    if created:
       profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)



def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 


