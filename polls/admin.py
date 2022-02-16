from django.contrib import admin

from .models import Choice, Question

# class QuestionChoiceAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['question']}),
#         (None, {'fields': ['choice']}),
#     ]
# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3
#
# class QuestionInline(admin.TabularInline):
#     model = Question
#     extra = 3

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['choice_text']}),
        (None, {'fields': ['votes']}),
    ]
    # inlines = [QuestionInline]
    list_display = ('choice_text', 'votes')
    # list_filter = ['pub_date']
    search_fields = ['choice_text']

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice, ChoiceAdmin)

# admin.site.register(QuestionChoice, QuestionChoiceAdmin)
