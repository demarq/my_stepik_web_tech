from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'login/', login, name='login'),
    url(r'logout/', logout, name='logout'),
    url(r'question/(?P<id>\d*)/$', question, name='question'),
    url(r'ask/', ask, name='ask'),
    url(r'signup/', signup, name='signup'),
    url(r'popular/', home, name='popular'),
    url(r'new/', test, name='new'),
]

