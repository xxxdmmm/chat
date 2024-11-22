from django.db import models


# Create your models here.

class userInfo(models.Model):
    username = models.CharField(max_length=30, verbose_name="姓名")
    password = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True, verbose_name="年龄")
    weight = models.DecimalField(null=True, blank=True, verbose_name="体重(Kg)", default=0, max_digits=10,
                                 decimal_places=4)
    high = models.DecimalField(null=True, blank=True, verbose_name="身高(m)", default=0, max_digits=10,
                               decimal_places=4)
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    sex = models.SmallIntegerField(verbose_name="性别", choices=gender_choices, default=1)
    phoneNumber = models.CharField(max_length=20, null=True, blank=True, verbose_name="电话")
    timestamp = models.DateTimeField(auto_now_add=True)
    first = models.BooleanField(default=True, verbose_name="第一次诊断")

    def __str__(self):
        return f"{self.username}\n{self.sex}\n{self.age}\n{self.phoneNumber}\n{self.timestamp}"


class Admin(models.Model):
    username = models.CharField(max_length=30, verbose_name="姓名")
    password = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=20, null=True, blank=True, verbose_name="电话")
    timestamp = models.DateTimeField(auto_now_add=True)
