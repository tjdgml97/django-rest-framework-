from django.contrib import admin
from . import models
from .models import Choice, Question

class ChoiceInline(admin.StackedInline):
    model = models.Choice
    extra = 1

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]


# admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Choice)
