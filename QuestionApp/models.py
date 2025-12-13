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
    time=models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name}: {self.creater.user.username}"
    
class SolvedQuestionGroup(models.Model):
    user=models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    question_group=models.ForeignKey(to=QuestionGroup, on_delete=models.CASCADE)
    score=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.user.username} - {self.question_group.name} - {self.score}"