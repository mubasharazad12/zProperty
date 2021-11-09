from django.contrib import admin
from .models import Question


# Register your models here


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone", "posted_date"]


admin.site.register(Question, QuestionAdmin)
