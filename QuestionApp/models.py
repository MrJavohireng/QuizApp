from django.db import models
from UserApp.models import Profile
answers=[("A","A"),("B","B"),("C","C"),("D","D")]
class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1, choices=answers)
    

    def __str__(self):
        return self.question_text
class QuestionGroup(models.Model):
    name = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question)
    creater=models.ForeignKey(to=Profile, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name}: {self.creater.user.username}"