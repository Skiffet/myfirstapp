from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):  # or admin.StackedInline for stacked layout
    model = Choice
    extra = 3  # Number of extra blank choice forms

class QuestionAdmin(admin.ModelAdmin):
    # Reorder fields
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]  # Include Choices inline
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']  # Sidebar filter
    search_fields = ['question_text']  # Search box

admin.site.register(Question, QuestionAdmin)
