from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
# def projects(request):
#     return HttpResponse("Here Our Products")


projectLists = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional Website',
    },
    {
        'id': '2',
        'title': 'Portfolio  Website',
        'description': 'Fully Portfolio functional Website',
    },
    {
        'id': '3',
        'title': 'Gambling Website',
        'description': 'Fully Gambling functional Website',
    }
]


def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    # return render(request, 'projects/projects.html', {'page': page, 'message':msg})
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags= projectObj.tags.all()
    return render(request, 'projects/single-project.html', {'project': projectObj, 'tags':tags})
