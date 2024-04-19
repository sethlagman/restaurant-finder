from django.shortcuts import render, HttpResponse
from .utils.main import BusinessFinder, get_location

# Create your views here.
def home(request):
    """This is the home page"""

    ip = request.META.get("REMOTE_ADDR", "")

    #TODO: defaultLocation = get_location(ip) ENABLE THIS IN DEPLOYMENT
    
    defaultLocation = 'Manila'

    return render(request, 'home.html', {
        'defaultLocation': defaultLocation,
    })

def results(request):
    """This is the results page"""

    if request.method == 'POST':
        food_query = request.POST.get('food_search', '')
        place_query = request.POST.get('place_search', '')

        print(food_query, place_query)

    return render(request, 'results.html')