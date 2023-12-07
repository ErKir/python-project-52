from django.shortcuts import render


def index(request):
    return render(request, 'render/templates/index.html', {})
