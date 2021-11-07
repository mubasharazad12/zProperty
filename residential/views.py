from django.shortcuts import render

from residential.models import ResidentialProperties, ResidentialPropertiesImage, Amenitie


def propertyGrid(request):
    all_properties = ResidentialProperties.objects.all()
    context = {
        "all_prop": all_properties
    }
    return render(request, "property-grid.html", context=context)


def propertyDetail(request, id=0):
    plan = ResidentialProperties.objects.filter(id=id)[0]
    gallery = ResidentialPropertiesImage.objects.filter(property=plan)
    amanities = Amenitie.objects.filter(property=plan)
    context = {
        "plan": plan,
        "Gallery": gallery,
        "Ama": amanities
    }
    return render(request, "property-detail.html", context)
