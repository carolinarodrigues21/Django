from django.db import models

#Choice and QUestion objects create a Python database-acess API

#modes.___ -> type of data each field holds 
class Question(models.Model):
    #variables name will be used as the database column's name
    question_text = models.CharField(max_lenght = 200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
