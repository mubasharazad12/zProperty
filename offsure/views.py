from django.shortcuts import render
from offsure.models import OFFPlanAndInvestment
from offsure.models import OffPlanGallery, PaymentPlans


# Create your views here.

def offplan(request):
    plans_list = OFFPlanAndInvestment.objects.all()
    context = {
        "plans_list": plans_list
    }
    return render(request, "off-plan.html", context=context)


def offplandetail(request, planid):
    plan_detail = OFFPlanAndInvestment.objects.get(id=planid)
    headerImages = OffPlanGallery.objects.filter(plan=plan_detail)
    invesments = PaymentPlans.objects.filter(plan=plan_detail)
    print("[+] Plane Details is ", plan_detail)
    print("[+] Plane Images are ", headerImages)
    print("[+] invesments are ", invesments)
    context = {
        "plan_detail": plan_detail
    }
    return render(request, "off-plan-detail.html", context=context)
