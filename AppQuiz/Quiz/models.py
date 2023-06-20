from django.db import models

class Question(models.Model):

    text = models.TextField(verbose_name='Question text')

    def __str__(self):
        return self.text
    

class ChooseAnswer(models.Model):
    MAX_ANSWERS = 3

    question = models.ForeignKey(Question, related_name='questions', on_delete=models.CASCADE)
    correct_asnwer = models.BooleanField(verbose_name='Is it the correct answer?', default=False, null=False)
    text = models.TextField(verbose_name='Answer text')

    def __str__(self) -> str:
        return self.text




