import datetime

from django.db import models
from django.utils import timezone

class Challenge(models.Model):

    challenge_name = models.CharField(max_length = 200)
    challenge_description = models.TextField(blank = True, null = True)
    week_number = models.AutoField(primary_key=True)

    def __str__(self):
        return self.challenge_name

class Student(models.Model):

    project_list = []

    student_name = models.CharField(max_length = 200)
    completed_weeks = models.IntegerField(default = 1)
    current_week_in_progress = models.BooleanField(default=False)

    def __str__(self):
        return self.student_name

    def update_progress(self, week_number):
        self.completed_weeks.append(week_number)

#############################

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text
