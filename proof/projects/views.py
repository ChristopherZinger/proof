from django.shortcuts import render
from django.urls import reverse
from .models import Project, Task
from django.shortcuts import get_object_or_404
# Create your views here.

def projectDetailView(request,id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project=project)
    print(tasks)
    return render(request, 'projects/detail.html',{'project':project, 'tasks':tasks})
