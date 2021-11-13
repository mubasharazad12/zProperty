from django.shortcuts import render, redirect
from Accounts.forms import PropertyInquiryForm
from Accounts.models import PropertyInquiry
from residential.models import ResidentialProperties, ResidentialPropertiesImage, Amenitie


def propertyGrid(request):
    all_properties = ResidentialProperties.objects.all()
    context = {
        "all_prop": all_properties,
    }
    return render(request, "property-grid.html", context=context)


def propertyDetail(request, id=0):
    plan = ResidentialProperties.objects.filter(id=id)[0]
    gallery = ResidentialPropertiesImage.objects.filter(property=plan)
    amanities = Amenitie.objects.filter(property=plan)
    if request.method == "POST":
        form = PropertyInquiryForm(request.POST)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.property_type = "residentials"
            newform.property_name = plan.Title
            newform.save()
            return redirect('property-detail', id)
    form = PropertyInquiryForm()
    context = {
        "plan_detail": plan,
        "Galleries": gallery,
        "amentites": amanities,
        "formData": form
    }
    return render(request, "property-detail.html", context)
