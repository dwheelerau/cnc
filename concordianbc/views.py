from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'home.html')


def results_page(request):
    return render(request, 'results.html')


def about_page(request):
    return render(request, 'about.html')
