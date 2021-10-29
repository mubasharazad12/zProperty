from django.shortcuts import render
from offsure.models import OFFPlanAndInvestment, OffPlanGallery
from residential.models import RedsidentialProperties, ResidentialPropertiesImage
from .models import HomeDashboardSlider


# Create your views here.

def index(request):
    off_plan_properties = OFFPlanAndInvestment.objects.all()[:6]
    all_res_properties = RedsidentialProperties.objects.all()[:6]
    home_dashboard = HomeDashboardSlider.objects.all()
    context = {
        "offplan_all_properties": off_plan_properties,
        "home_dashboard": home_dashboard,
        "all_res_properties": all_res_properties
    }
    return render(request, "index.html", context)


def contact(request):
    return render(request, "contact.html")


def propertyGrid(request):
    all_properties = RedsidentialProperties.objects.all()
    context = {
        "all_prop": all_properties
    }
    return render(request, "property-grid.html", context=context)


def propertyDetail(request):
    return render(request, "property-detail.html")
