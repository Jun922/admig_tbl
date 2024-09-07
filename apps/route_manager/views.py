from django.shortcuts import render


def index(request):
    return render(request, 'route_manager/index.html')
