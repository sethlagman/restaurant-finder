from django.shortcuts import render, HttpResponse
from .utils.main import BusinessFinder

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

    ip = request.META.get("REMOTE_ADDR", "")

    #TODO: defaultLocation = get_location(ip) ENABLE THIS IN DEPLOYMENT

    defaultLocation = 'Manila'

    if request.method == 'POST':
        term_query = request.POST.get('term_search', '')
        place_query = request.POST.get('place_search', '')

    try:
        result = BusinessFinder(term_query, place_query)
        queried_info = zip(result.getName(), result.getLocation(), result.getRating(), result.getImage())
    except KeyError: # Handling error when there are no results foud or invalid input
        return HttpResponse("Error")
    else:
        return render(request, 'results.html', {
            'defaultLocation': defaultLocation,
            'term_query': term_query,
            'place_query': place_query,
            'info': queried_info,
        })