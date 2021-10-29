from django.contrib import admin
from .models import ResidentialPropertiesImage, ResidentialProperties, Amenitie


# Register your models here.


class InlineResidentialImages(admin.TabularInline):
    model = ResidentialPropertiesImage


class InlineAmenitie(admin.TabularInline):
    model = Amenitie


class InlineResidentialPro(admin.ModelAdmin):
    inlines = [InlineResidentialImages, InlineAmenitie]


admin.site.register(ResidentialProperties, InlineResidentialPro)
