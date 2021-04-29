from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'app/index.html')


def page2(request):
    return render(request, 'app/page2.html')
