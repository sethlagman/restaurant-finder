from django.shortcuts import render, HttpResponse
from .utils.main import BusinessFinder, get_location, digitalOcean_ip

# Create your views here.
def home(request):
    """This is the home page"""

    defaultLocation = get_location(digitalOcean_ip(request))
    
    #* defaultLocation = 'Japan'

    return render(request, 'home.html', {
        'defaultLocation': defaultLocation,
    })

def results(request):
    """This is the results page"""
    
    defaultLocation = get_location(digitalOcean_ip(request))

    #* defaultLocation = 'Japan'

    if request.method == 'POST':
        term_query = request.POST.get('term_search', '')
        place_query = request.POST.get('place_search', '')

    place = place_query if place_query else defaultLocation

    try:
        result = BusinessFinder(term_query, place)
        queried_info = zip(result.getName(), result.getLocation(), result.getRating(), result.getImage(), result.getUrl())
    except KeyError: # Handling error when there are no results foud or invalid input
        return HttpResponse("Error")
    else:
        return render(request, 'results.html', {
            'defaultLocation': defaultLocation,
            'term_query': term_query,
            'place_query': place_query,
            'info': queried_info,
        })