# Generated by Django 4.2 on 2024-07-25 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_info_new', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentMedicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('symptoms', models.TextField(blank=True, null=True, verbose_name='既往病史')),
                ('change_notes', models.TextField(blank=True, null=True, verbose_name='本次信息的修改说明')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('symptom', models.TextField(blank=True, null=True, verbose_name='症状')),
                ('prescription', models.TextField(blank=True, null=True, verbose_name='处方')),
                ('additional_notes', models.TextField(blank=True, null=True, verbose_name='其他补充')),
                ('change_notes', models.TextField(blank=True, null=True, verbose_name='本次信息的修改说明')),
            ],
        ),
    ]