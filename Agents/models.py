from django.db import models


# Create your models here.

class Agent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to="Agents/Profiles")
    description = models.TextField()

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
