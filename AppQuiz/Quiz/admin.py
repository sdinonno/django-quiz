from django.contrib import admin
from .models import Question, ChooseAnswer

class ChooseAnswerInLine(admin.TabularInline):
    model = ChooseAnswer
    max_num = ChooseAnswer.MAX_ANSWERS
    min_num = ChooseAnswer.MAX_ANSWERS

class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = (ChooseAnswerInLine, )
    list_display = ['text',]
    search_fields = ['text', 'questions__text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(ChooseAnswer)
