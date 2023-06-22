from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    ALLOWED_ANSWERS = 1
    text = models.TextField(verbose_name='Question text')

    def __str__(self):
        return self.text
    

class ChooseAnswer(models.Model):
    MAX_ANSWERS = 3

    question = models.ForeignKey(Question, related_name='questions', on_delete=models.CASCADE)
    correct_answer = models.BooleanField(verbose_name='Is it the correct answer?', default=False, null=False)
    text = models.TextField(verbose_name='Answer text')

    def __str__(self) -> str:
        return self.text
    
class QuestionAttempts(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(ChooseAnswer, on_delete=models.CASCADE, related_name='attempts')
    correct_answer = models.BooleanField(verbose_name='Is it the correct answer?', default=False, null=False)
    score = models.DecimalField(verbose_name='Score', default=0, decimal_places=2, max_digits=6)

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_score = models.DecimalField(verbose_name='Total Score', default=0, decimal_places=2, max_digits=10)





