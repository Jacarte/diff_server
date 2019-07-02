from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
# Create your views here.

def index(request):
    
    #https://github.com/mhutch/MonoDevelop.MSBuildEditor/compare/bc0201e4ebf7...e31f5d523c37.diff

    url = request.GET.get('url', None)

    with urllib.request.urlopen(url) as response:
        html = response.read()
        return HttpResponse(html)
    return HttpResponse('Fail')