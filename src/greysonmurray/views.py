"""
src/greysonmurray/views.py
"""

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from greysonmurray.models import Project


def index(request):
	projects = Project.objects.all()
	context = {"projects": projects}
	return render(request, 'projects/index.html', context)

def project(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	return render(request, 'projects/detail.html', {'project':project})