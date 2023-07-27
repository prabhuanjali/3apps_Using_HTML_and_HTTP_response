from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def first(request):
    return render(request, 'first.html')

def first1(request):
    return HttpResponse('Helloooooooo!!!!!!!!')

def second(request):
    return render(request, 'second.html')

def second1(request):
    return HttpResponse('Byeeeeeeeee!!!!!!!!')