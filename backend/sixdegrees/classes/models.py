from django.db import models
from django.contrib.auth.models import User

counter = 0

class UserProfile(models.Model):
	user = models.OneToOneField(User)

class NPOProfile(models.Model):
	user = models.OneToOneField(User) 
	camp_id = models.SmallIntegerField(null = True, blank = True)

class Campaign(models.Model):
	camp_id = models.SmallIntegerField(default = counter)
	counter = counter + 1;
	title = models.CharField(max_length=200)
	story_tell = models.TextField(max_length=256, null=False, blank=False)
	action1 = models.CharField(max_length=200)
	action2 = models.CharField(max_length=200)
	action3 = models.CharField(max_length=200)
	catalyst = models.ForeignKey(UserProfile, blank=False)
	npo_user = models.ForeignKey(NPOProfile, blank = False)
	user_1 = models.CharField(max_length=200, null = True, blank = True)
	user_2 = models.CharField(max_length=200, null = True, blank = True)
	user_3 = models.CharField(max_length=200, null = True, blank = True)
	user_4 = models.CharField(max_length=200, null = True, blank = True)
	user_5 = models.CharField(max_length=200, null = True, blank = True)
	user_6 = models.CharField(max_length=200, null = True, blank = True)
