from django.db import models
from account.models import CustomUser


# Create your models here.

class Subject(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Group(models.MOdel):
    students = models.ForeignKey('CustomUser', on_delete=models.CASCADE())
    mentor = models.ForeignKey('CustomUser', on_delete=models.CASCADE())
    days = models.DateField()
    time = models.DateField()
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE())
