from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    # return HttpResponse("Howdy")
    return render(request, "core/index.html")



