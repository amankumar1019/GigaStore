from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "blog/index.html")


def google(request):
    content = "www.google.com"
    return HttpResponse(content)