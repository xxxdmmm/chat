from django.db import models


# Create your models here.

class department(models.Model):
    department_name = models.CharField(max_length=20)

    def __str__(self):
        return self.department_name


class hospital(models.Model):
    hospital_name = models.CharField(max_length=30)
    area = models.CharField(max_length=30, null=True, blank=True)


class doctorInfos(models.Model):
    doctor_name = models.CharField(max_length=30, verbose_name="账户")
    password = models.CharField(max_length=50, verbose_name="密码")
    department = models.ForeignKey(to="department", to_field="id", on_delete=models.CASCADE, verbose_name="科室")
    photo_path = models.CharField(max_length=100,
                                  default='static/loginAndRegister/img/default.png', blank=True, null=True)
    hospital = models.CharField(max_length=50, null=True, blank=True, verbose_name="医院")
    age = models.IntegerField(null=True, blank=True, verbose_name="年龄")
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    sex = models.SmallIntegerField(verbose_name="性别", choices=gender_choices, default=1)
    phoneNumber = models.CharField(max_length=20, verbose_name="电话", blank=True, null=True)
    introduction = models.TextField(null=True, blank=True, verbose_name="简介(选填)")
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="创建时间")
