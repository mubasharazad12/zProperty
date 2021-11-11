from django.shortcuts import render, redirect
from offsure.models import OFFPlanAndInvestment
from residential.models import ResidentialProperties
from .models import HomeDashboardSlider
from Agents.models import Agent
from Accounts.forms import QuestionForm


# Create your views here.

def index(request):
    off_plan_properties = OFFPlanAndInvestment.objects.all().order_by('uploaded_date')
    all_res_properties = ResidentialProperties.objects.all().order_by('uploaded_date')
    home_dashboard = HomeDashboardSlider.objects.all()
    agents = Agent.objects.all()
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    form = QuestionForm()
    context = {
        "offplan_all_properties": off_plan_properties,
        "home_dashboard": home_dashboard,
        "all_res_properties": all_res_properties,
        "agents": agents,
        "form": form
    }
    return render(request, "index.html", context)


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")
