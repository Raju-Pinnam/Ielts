from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Question(models.Model):
    """Basic Quesions type of question 
        is may be mp3, text, which
    """
    video_type = models.FileField(blank=True,
                                  null=True,
                                  upload_to="")
    audio_type = models.FileField(blank=True,
                                  null=True,
                                  upload_to="")
    text_type = models.FileField(blank=True,
                                  null=True,
                                  upload_to="")


class Answer(models.Model):
    """
    Answer For the question
    """
    quesion = models.ForeignKey(Question, on_delete=models.CASCADE,
                                null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    

class TestPaper(models.Model):
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    total_marks = models.IntegerField(default=0)


class TestUser(models.Model):
    test_paper = models.ForeignKey(TestPaper, on_delete=models.CASCADE,
                                   null=True, blank=True)
    attendent = models.ForeignKey(User, on_delete=models.CASCADE,
                                  null=True, blank=True)
    gained_marks = models.DecimalField(max_digits=4,
                                       decimal_places=2, default=0.00)
    is_attended = models.BooleanField(default=False)
    
    