from django.db import models


# Create your models here.
class UserPharmacy(models.Model):
    belong = models.BigIntegerField(default=1, verbose_name="归属")
    doctor_name = models.CharField(max_length=30, verbose_name="医生名称")
    user_name = models.CharField(max_length=30, verbose_name="患者名称")
    crawl_name = models.ForeignKey(to="CrawlPeople", to_field="id", on_delete=models.CASCADE, verbose_name="抓药师")
    check_name = models.ForeignKey(to="CheckPeople", to_field="id", on_delete=models.CASCADE, verbose_name="监管确认")
    photo_path = models.CharField(max_length=200,
                                  default='pharmacy_image/default.png', blank=True, null=True)
    symptom = models.CharField(max_length=2000, blank=True, null=True)
    prescription = models.CharField(max_length=2000, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="创建时间")


class CrawlPeople(models.Model):
    name = models.CharField(max_length=30, verbose_name="姓名")
    password = models.CharField(max_length=50, verbose_name="密码")
    phoneNumber = models.CharField(max_length=20, verbose_name="电话", blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="创建时间")

    def __str__(self):
        return self.name


class CheckPeople(models.Model):
    name = models.CharField(max_length=30, verbose_name="姓名")
    password = models.CharField(max_length=50, verbose_name="密码")
    phoneNumber = models.CharField(max_length=20, verbose_name="电话", blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="创建时间")

    def __str__(self):
        return self.name
