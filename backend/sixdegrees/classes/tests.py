from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from classes.models import Campaign
from classes.models import UserProfile
from classes.models import NPOProfile

class UserProfile(TestCase):

	def setUp(self):
		"""Lets create one User Profile that we can use within the tests below"""
		person = User.objects.create_user(username='john', email='jlennon@beatles.com', password='codeforgood')
		self.example_user = UserProfile.objects.create(user = User.objects.get(username = 'john'))
	
	def test_model_fields_exist(self):
		self.assertTrue(1==1)

class NPOProfile(TestCase):

    def setUp(self):
        """Lets create one NPO Profile that we can use within the tests below"""
        person = User.objects.create_user(username='ringo', email='rstarr@beatles.com', password='codeforgood')
        self.example_npo = NPOProfile.objects.create(user = User.objects.get(username = 'ringo'))

class Campaign(TestCase):

    def setUp(self):
        """Lets create one campaign that we can use within the tests below"""
        c = UserProfile.objects.get(username='john')
        n = NPOProfile.objects.get(username = 'ringo')
        self.example_camp = Campaign.create(camp_id = 1, title = 'campaign', story = 'support my cause',
        	action1 = 'donate', action2 = 'volunteer', action3 = 'share', catalyst = c, npo_user = n)
