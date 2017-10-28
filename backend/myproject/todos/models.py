from django.db import models
# Leverage Django's built-in User models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):  
    user = models.OneToOneField(User)  
    campaign = models.ForeignKey(Campaigns, null=True, blank=True)

    def __str__(self):  
          return "%s's profile" % self.user  

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 


class NPOProfile(models.Model):  
    npo_user = models.OneToOneField(User)  
   	campaign = models.ForeignKey(Campaigns, null=True, blank=True)  

    def __str__(self):  
          return "%s's profile" % self.user  

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 


class Campaigns(models.Model):

    user = models.ForeignKey(User, null=True, blank=True)
    npo = models.ForeignKey(NPOProfile, null=True, blank=True)
    actions = models.CharField(max_length=128, null=False, blank=False)
    date_created = models.DateField(null=True, blank=True)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description
