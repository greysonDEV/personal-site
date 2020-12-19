"""
src/greysonmurray/urls.py
"""

from django.urls import path
from greysonmurray import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:project_id>/', views.project, name="project")
]