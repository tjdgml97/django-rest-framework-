# from django.db import models

# # Create your models here.
# class Question(models.Model) :
#     question_text=models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
# #Question 을 지울때 - 같이 지우거나 , question이 남아있을때는 지우지 못하게 : CASCADE


from django.db import models
