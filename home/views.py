from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def propertyGrid(request):
    return render(request, "property-grid.html")

def propertyDetail(request):
    return render(request, "property-detail.html")