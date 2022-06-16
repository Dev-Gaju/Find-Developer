from django.shortcuts import render
from django.http import HttpResponse

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
    msg = "Hello, you are on the project page"
    page = 12
    number = 10
    context = {
        'page': page,
        'message': msg,
        'number': number,
        'projects': projectLists
    }
    # return render(request, 'projects/projects.html', {'page': page, 'message':msg})
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None
    for i in projectLists:
        if i["id"] == pk:
            projectObj = i

    return render(request, 'projects/single-project.html', {'project' : projectObj})
