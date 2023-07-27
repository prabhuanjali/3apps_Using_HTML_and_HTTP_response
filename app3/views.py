from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def fifth(request):
    return render(request, 'fifth.html')

def fifth1(request):
    return HttpResponse('NOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!')

def sixth(request):
    return render(request, 'sixth.html')

def sixth1(request):
    return HttpResponse('NOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!')