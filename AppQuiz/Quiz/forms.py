from django import forms

from .models import Question, ChooseAnswer, QuestionAttempts

class ChooseInlineFormset(forms.BaseInlineFormSet):
    def clean(self) -> None:
        super(ChooseInlineFormset, self).clean()

        correct_answer = 0
        for form in self.forms:
            if not form.is_valid():
                return
            
            if form.cleaned_data and form.cleaned_data.get('correct') is True:
                correct_answer += 1

        try:
            assert correct_answer == Question.ALLOWED_ANSWERS
        except AssertionError:
            raise forms.ValidationError('Only one answer is allowed.')


    
