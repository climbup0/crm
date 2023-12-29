from django.db import models
from account.models import CustomUser
# Create your models here.

class Payment(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE())
    lebel = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.user

#davomida ulanadigan narsala yo'q yo'qlamani ozim yozaman