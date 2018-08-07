from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'login/', test, name='login'),
    url(r'question/(?P<id>\d*)$', question, name='question'),
    url(r'ask/', test, name='ask'),
    url(r'signup/', test, name='signup'),
    url(r'popular/', home, name='popular'),
    url(r'new/', test, name='new'),
]

