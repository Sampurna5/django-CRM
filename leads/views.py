from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    # return HttpResponse("Hello World!!")
    return render(request, 'second_index.html')
