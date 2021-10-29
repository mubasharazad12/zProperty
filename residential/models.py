from django.db import models


# Create your models here.


class ResidentialProperties(models.Model):
    Title = models.CharField(max_length=100)
    overview = models.TextField()
    Dashboard_Image = models.ImageField(upload_to="ResidentialInvesment", null=True)
    Price = models.CharField(max_length=100)
    Area = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    num_bedRooms = models.CharField(max_length=100)
    num_WashRooms = models.CharField(max_length=100)
    num_Garage = models.CharField(max_length=100, null=True)
    video_url = models.TextField(null=True)
    property_type = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return str(self.Title)


class ResidentialPropertiesImage(models.Model):
    property = models.ForeignKey(ResidentialProperties, models.CASCADE)
    description = models.TextField(null=True)
    Image = models.ImageField(upload_to="ResidentialInvesment/Gallery")

    def __str__(self) -> str:
        return str(self.property)


class Amenitie(models.Model):
    property = models.ForeignKey(ResidentialProperties, models.CASCADE)
    name = models.CharField(max_length=100)
