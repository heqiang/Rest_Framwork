from django.db import models


# Create your models here.


class Movie(models.Model):
    Name = models.CharField(max_length=125)
    Url = models.CharField(max_length=120)
    Quote = models.CharField(max_length=220)
    Star = models.CharField(max_length=20)


class UserInfo(models.Model):
    user_type_choince = (
        ("1", "普通用户"),
        ("2", "vip"),
        ("3", "svip")
    )
    user_type = models.IntegerField(choices=user_type_choince)
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=32)


class UserToken(models.Model):
    user = models.OneToOneField(UserInfo,primary_key=True,on_delete=models.CASCADE)
    token = models.CharField(max_length=64)