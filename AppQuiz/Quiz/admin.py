from django.contrib import admin
from .models import Question, ChooseAnswer, QuestionAttempts
from .forms import ChooseInlineFormset

class ChooseAnswerInLine(admin.TabularInline):
    model = ChooseAnswer
    can_delete = False
    max_num = ChooseAnswer.MAX_ANSWERS
    min_num = ChooseAnswer.MAX_ANSWERS
    formset = ChooseInlineFormset

class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = (ChooseAnswerInLine, )
    list_display = ['text',]
    search_fields = ['text', 'questions__text']

class QuestionAttemptsAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'correct', 'score']

    class Target:
        model = QuestionAttempts

admin.site.register(QuestionAttempts)
admin.site.register(Question, QuestionAdmin)
admin.site.register(ChooseAnswer)
