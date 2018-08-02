from django.conf.urls import url
from qa.views import test

urlpatterns = [
    url(r'^$', test, name='home'),
    url(r'login/', test, name='login'),
    url(r'question/(?P<id>[\d]{0,10})$', test, name='question'),
    url(r'ask/', test, name='ask'),
    url(r'signup/', test, name='signup'),
    url(r'popular/', test, name='popular'),
    url(r'new/', test, name='new'),
]

