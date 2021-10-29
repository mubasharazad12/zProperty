from django.db import models


# Create your models here.
class HomeDashboardSlider(models.Model):
    heading = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to="HomeDashboard")

    def __str__(self):
        return self.heading
