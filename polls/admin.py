from django.contrib import admin

from .models import Choice, Question, QuestionChoice


class QuestionChoiceInline(admin.TabularInline):
    model = QuestionChoice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = (QuestionChoiceInline,)


class ChoiceAdmin(admin.ModelAdmin):
    inlines = (QuestionChoiceInline,)

# class ChoiceAdmin(admin.ModelAdmin):
#     pass
#
#
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#     list_filter = ['pub_date']
#     search_fields = ['question_text']


admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionChoice)
