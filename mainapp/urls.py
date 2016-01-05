from django.conf.urls import url
from . import views

'''
Created on Jan 5, 2016

@author: otrujilx
'''

urlpatterns = {
   url(r'^$', views.index, name='index')
}