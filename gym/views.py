from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'gym/index.html')


def about(request):
    return render(request, 'gym/about.html')


def blog(request):
    return render(request, 'gym/blog.html')


def klass(request):
    return render(request, 'gym/class.html')


def contact(request):
    return render(request, 'gym/contact.html')


def feature(request):
    return render(request, 'gym/feature.html')


def single(request):
    return render(request, 'gym/single.html')


