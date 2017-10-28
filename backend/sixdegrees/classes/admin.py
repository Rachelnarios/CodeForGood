from django.contrib import admin

# Register your models here.
from .models import Campaign
from .models import UserProfile
from .models import NPOProfile

admin.site.register(Campaign)
admin.site.register(UserProfile)
admin.site.register(NPOProfile)