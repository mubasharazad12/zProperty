from django.contrib import admin
from .models import Question, Answers


# Register your models here.

class AnswersAdmin(admin.TabularInline):
    model = Answers


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswersAdmin]


admin.site.register(Question, QuestionAdmin)
