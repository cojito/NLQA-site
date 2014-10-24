from django.db import models

# Create your models here.
class Query(models.Model):
    question_text = models.CharField(max_length=250)
    answer_text = models.CharField(max_length=250)
    correctness = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)

    # def __str__(self):
    # 	q = "Question: " + self.question_text + "\n" + "Answer: " + self.answer_text + "\n"
    #     return q


