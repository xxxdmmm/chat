# Generated by Django 4.2 on 2024-07-26 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_info_new', '0004_choose_alter_howmangbig_bowel_movements_frequency_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TABLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('TEST', models.BooleanField(default=False, verbose_name='TEST')),
            ],
        ),
    ]