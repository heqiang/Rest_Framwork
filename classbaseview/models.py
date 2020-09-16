from django.db import models


# Create your models here.

class UserGroup(models.Model):
    title = models.CharField(max_length=32)


class UserInfo(models.Model):
    user_type_choince = (
        (1, "普通用户"),
        (2, "vip"),
        (3, "svip")
    )
    user_type = models.IntegerField(choices=user_type_choince)
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=32)
    group = models.ForeignKey(UserGroup,on_delete=models.CASCADE)
    roles = models.ManyToManyField("Role")


class UserToken(models.Model):
    user = models.OneToOneField(UserInfo,primary_key=True,on_delete=models.CASCADE)
    token = models.CharField(max_length=64)

class Role(models.Model):
        title = models.CharField(max_length=32)