from django.shortcuts import render
from offsure.models import OFFPlanAndInvestment, OffPlanGallery


# Create your views here.

def index(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")


def propertyGrid(request):
    # This is just for one Element
    all_properties = OFFPlanAndInvestment.objects.all()
    context = {
        "demoImage": all_properties[0].Dashboard_Image,
        "Title": all_properties[0].PlanName,
        "OverView": all_properties[0].Overview,
        "Price": all_properties[0].Price
    }
    # For All Element U Need to Loop On all_prop
    # all_properties = OFFPlanAndInvestment.objects.all()
    # context = {
    #     "all_prop": all_properties
    # }
    return render(request, "property-grid.html", context=context)


def propertyDetail(request):
    return render(request, "property-detail.html")
