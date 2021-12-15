#from typing_extensions import Required
#from typing_extensions import Required
from django.db import models
from django.http import request
from accounts.models import User_user

# Create your models here.

CATEGORY = (('japanese','国語'),('math','数学'),('english','英語'),('social_study','現代社会'),('chemistry','化学'),('biology','生物'),('physics','物理'),('other','その他'))
class PrintModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User_user, on_delete=models.CASCADE)
    images = models.FileField(upload_to='file/%Y/%m/%d')
    category = models.CharField(
        max_length = 50,
        choices = CATEGORY,
        default=CATEGORY[0][0]
    )

    def __str__(self):
        return self.title[:40]


class Comment(models.Model):
    name = models.ForeignKey(User_user, on_delete=models.CASCADE)
    content = models.TextField('本文')
    target = models.ForeignKey(PrintModel, on_delete=models.CASCADE, verbose_name='対象の投稿')

    def __str__(self):
        return self.content[:20]
