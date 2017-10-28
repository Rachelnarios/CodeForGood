from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


urlpatterns = [
    url(r'^accounts/login/', LoginView.as_view(template_name='classes/UI/Webpage/examples/userlogin.html'), name="userlogin"),
    url(r'^accounts/nplogin/', LoginView.as_view(template_name='classes/UI/Webpage/examples/NPsignup-page.html'), name='np-signup'),
    url(r'^accounts/logout/', LogoutView.as_view(), name="user_logout"),
#    url(r'^accounts/register/', CreateView.as_view(
#            template_name='registration/register.html',
#            form_class=UserCreationForm,
#            success_url='/'
#    )),
    url(r'^accounts/register/', CreateView.as_view(template_name='classes/UI/Webpage/examples/signup-page.html', form_class=UserCreationForm, success_url='/'), name = 'signup-page'),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('classes.urls'), name = 'homepage'),
]