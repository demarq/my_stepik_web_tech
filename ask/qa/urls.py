from django.urls import path, include
from qa.views import test

urlpatterns = [
    path(r'^/', test, name='home'),
    path(r'^login/', test, name='login'),
    path(r'^question/?P<id>(\d*)', test, name='question'),
    path(r'^ask/', test, name='ask'),
    path(r'^popular/', test, name='popular'),
    path(r'^new/', test, name='new'),
]

