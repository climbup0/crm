from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

STUDENT, TEACHER, ADMIN = "student", "teacher", "admin"


class CustomUser(AbstractUser):
    USER_RULES = (
        (STUDENT, STUDENT),
        (TEACHER, TEACHER),
        (ADMIN, ADMIN)
    )
    user_role = models.CharField(max_length=10, choices=USER_RULES)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user_info = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    hisob = models.IntegerField()
    bio = models.TextField()
    dagavor = models.FileField()

    def __str__(self):
        return self.user_info


