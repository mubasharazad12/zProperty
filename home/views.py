from django.shortcuts import render
from offsure.models import OFFPlanAndInvestment
from residential.models import ResidentialProperties
from .models import HomeDashboardSlider
from Agents.models import Agent


# Create your views here.

def index(request):
    off_plan_properties = OFFPlanAndInvestment.objects.all().order_by('uploaded_date')
    all_res_properties = ResidentialProperties.objects.all().order_by('uploaded_date')
    home_dashboard = HomeDashboardSlider.objects.all()
    agents = Agent.objects.all()
    # print("[+] off_plan_properties are ", off_plan_properties)
    # print("[+] residential properties are ", all_res_properties)
    context = {
        "offplan_all_properties": off_plan_properties,
        "home_dashboard": home_dashboard,
        "all_res_properties": all_res_properties,
        "agents": agents
    }
    return render(request, "index.html", context)


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")
