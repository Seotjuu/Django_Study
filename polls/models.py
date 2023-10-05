import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)    # 질문 내용 문자, 200자까지
    pub_date = models.DateTimeField("date published")   # 날짜

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        # 현재 시간 - 현재 전날의 시간
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 질문이 삭제가 되면 같이 삭제됨
    choice_text = models.CharField(max_length=200) # 문자열 200자까지
    votes = models.IntegerField(default=0) # 숫자 기본값 0
    
    def __str__(self):
        return self.choice_text
    