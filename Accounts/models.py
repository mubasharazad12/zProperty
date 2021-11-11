from django.db import models


# Create your models here.

class Question(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    posted_date = models.DateTimeField(auto_now=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Question = models.TextField(null=True)


class PropertyInquiry(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    posted_date = models.DateTimeField(auto_now=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Question = models.TextField(null=True)
    property_type = models.CharField(max_length=100, null=True, blank=True)
    property_name = models.CharField(max_length=100, null=True, blank=True)