# Generated by Django 4.2 on 2024-07-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0003_userpharmacy_prescription_userpharmacy_symptom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpharmacy',
            name='photo_path',
            field=models.CharField(blank=True, default='pharmacy_image/default.png', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userpharmacy',
            name='prescription',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='userpharmacy',
            name='symptom',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]