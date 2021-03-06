from django.db import models
import datetime # for was_published_recently
from django.utils import timezone # for was_published_recently

# Create your models here.

class MyQuestion(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now-datetime.timedelta(days=1) <=self.pub_date <= now
        #return self.pub_date>= timezone.now()-datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.shord_description = 'Published recently?'

class MyChoice(models.Model):
    question = models.ForeignKey(MyQuestion, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
