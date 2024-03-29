from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    """This is the home page"""

    return render(request, 'home.html')

def results(request):
    """This is the results page"""

    return render(request, 'results.html')