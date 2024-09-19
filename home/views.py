from django.shortcuts import render
from django.core.cache import cache
from django.http import HttpResponse

# Create your views here.
def index(request):
    """
    A view to index page 
    """
    return render(request, 'home/index.html')

def clear_cache(request):
    cache.clear()
    return HttpResponse("Cache cleared!")