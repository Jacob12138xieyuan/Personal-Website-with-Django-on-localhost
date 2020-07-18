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
    createForm = ProjectForm()
    if request.method == 'POST':
        createForm = ProjectForm(request.POST, request.FILES)
        if createForm.is_valid():
            createForm.save()
            print("create successful")
            return redirect('homePage')
        else:
            print("invalid form, fill in again...")
    return render(request, 'createPage.html', {'createForm': createForm})


def editPage(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    editForm = ProjectForm(instance=project)
    if request.method == 'POST':
        editForm = ProjectForm(request.POST, request.FILES, instance=project)
        if editForm.is_valid():
            editForm.save()
            print("edit successful")
            return redirect('homePage')
        else:
            print("invalid form, fill in again...")
    return render(request, 'editPage.html', {'editForm': editForm})
