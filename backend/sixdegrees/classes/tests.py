from django.test import TestCase
from django.test.client import Client

from .models import Campaign
from .models import UserProfile
from .models import NPOProfile

class UserProfile(TestCase):

    def setUp(self):
        """Lets create one todo that we can use within the tests below"""
        person = User.objects.create_user(username='john',
                                 email='jlennon@beatles.com',
                                 password='codeforgood')
        self.example_user = UserProfile.objects.create(user = person)

class NPOProfile(TestCase):

    def setUp(self):
        """Lets create one todo that we can use within the tests below"""
        person = User.objects.create_user(username='ringo',
                                 email='rstarr@beatles.com',
                                 password='codeforgood')
        self.example_npo = NPOProfile.objects.create(user = person)

class Campaign(TestCase):

    def setUp(self):
        """Lets create one todo that we can use within the tests below"""
        
        self.example_camp = Campaign.objects.create(camp_id = 1, title = 'campaign', story = 'support my cause',
        	action1 = 'donate', action2 = 'volunteer', action3 = 'share', catalyst = , npo_user =  )
