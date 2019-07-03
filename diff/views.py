from django.shortcuts import render
from django.http import JsonResponse
from urllib.request import urlopen

from unidiff import PatchSet

# Create your views here.

def completeDif(request):
    
    #https://github.com/mhutch/MonoDevelop.MSBuildEditor/compare/bc0201e4ebf7...e31f5d523c37.diff

    url = request.GET.get('url', None)

    with urlopen(url) as diff:
        #print(diff.headers)
        #encoding = diff.headers.getparam('charset')
        #s = PatchSet(diff, encoding='utf-8')
        #print(len(s))
        return JsonResponse({'body': diff.read().decode("utf-8")})
    return HttpResponse('Fail')


def onlyMeta(request):
    
    #https://github.com/mhutch/MonoDevelop.MSBuildEditor/compare/bc0201e4ebf7...e31f5d523c37.diff

    url = request.GET.get('url', None)

    with urlopen(url) as diff:
        #print(diff.headers)
        #encoding = diff.headers.getparam('charset')
        s = PatchSet(diff, encoding='utf-8')
        #print(len(s))
        return JsonResponse({'body': [
            dict( added = patch.added, removed=patch.removed) for patch in s
        ]})
    return HttpResponse('Fail')