from django.db import models
from account.models import CustomUser
from category.models import Group
# Create your models here.


class Lesson(models.Model):
    group = models.ForeignKey('Group', on_delete=models.CASCADE())
    video = models.FileField()
    caption = models.TextField()
    file = models.FileField()

    def __str__(self):
        return self.group

class Vazifa(models.Model):
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE())
    file = models.FileField()
    izoh = models.TextField()