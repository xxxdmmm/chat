# Generated by Django 4.2 on 2024-07-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginAndRegister', '0006_userinfo_first'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='first',
            field=models.BooleanField(default=True, verbose_name='第一次诊断'),
        ),
    ]