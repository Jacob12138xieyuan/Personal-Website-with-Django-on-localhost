from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
# Create your views here.


def homePage(request):
    projects = Project.objects.all()
    return render(request, 'homePage.html', {'projects': projects})


def detailPage(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'detailPage.html', {'project': project})


def createPage(request):
    createForm = ProjectForm(request.POST)
    return render(request, 'createPage.html', {'createForm': createForm})


def editPage(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(instance=project)
    #form = EditForm()
    #project = get_object_or_404(Project, pk=project_id)
    return render(request, 'editPage.html', {'project': project})
