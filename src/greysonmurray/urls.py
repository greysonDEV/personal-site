"""
src/greysonmurray/urls.py
"""

from django.urls import path
from greysonmurray import views

urlpatterns = [
	path('', views.index, name='index')
]