from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def third (request):
    return render(request, 'third.html')

def third1(request):
    return HttpResponse('Ohhh NOOOOOOOOOOOOOOO!!!!!!')

def fourth(request):
    return render(request, 'fourth.html')

def fourth1(request):
    return HttpResponse('Hiiiiiiiiiiiiiiiiiiiiiiiiii')