# Generated by Django 4.2 on 2024-06-21 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_info', '0005_alter_result_belong'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bowelandurinarysymptoms',
            name='belong',
            field=models.CharField(default=1, max_length=20, verbose_name='是谁的'),
        ),
        migrations.AlterField(
            model_name='coldandhot',
            name='belong',
            field=models.CharField(default=1, max_length=20, verbose_name='是谁的'),
        ),
        migrations.AlterField(
            model_name='currentmedicalhistory',
            name='belong',
            field=models.CharField(default=1, max_length=20, verbose_name='是谁的'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dietcondition',
            name='belong',
            field=models.CharField(default=1, max_length=20, verbose_name='是谁的'),
        ),
        migrations.AlterField(
            model_name='gynecologicalsymptoms',
            name='belong',
            field=models.CharField(default=1, max_length=20, verbose_name='是谁的'),
        ),
        migrations.AlterField(
            model_name='headnosemouth',
            name='belong',
            field=models.CharField(default=1, max_length=20, verbose_name='是谁的'),
        ),
        migrations.AlterField(
            model_name='numbnesssymptoms',
            name='belong',
            field=models.CharField(default=1, max_length=20, verbose_name='是谁的'),
        ),
        migrations.AlterField(
            model_name='physicalstrength',
            name='belong',
            field=models.CharField(default=1, max_length=20, verbose_name='是谁的'),
        ),
        migrations.AlterField(
            model_name='result',
            name='belong',
            field=models.CharField(default=1, max_length=20, verbose_name='是谁的'),
        ),
        migrations.AlterField(
            model_name='sleepdisorder',
            name='belong',
            field=models.CharField(default=1, max_length=20, verbose_name='是谁的'),
        ),
        migrations.AlterField(
            model_name='sweat',
            name='belong',
            field=models.CharField(default=1, max_length=20, verbose_name='是谁的'),
        ),
        migrations.AlterField(
            model_name='thirst',
            name='belong',
            field=models.CharField(default=1, max_length=20, verbose_name='是谁的'),
        ),
        migrations.AlterField(
            model_name='tongueappearance',
            name='belong',
            field=models.CharField(default=1, max_length=20, verbose_name='是谁的'),
        ),
        migrations.AlterField(
            model_name='urologicalsymptoms',
            name='belong',
            field=models.CharField(default=1, max_length=20, verbose_name='是谁的'),
        ),
        migrations.AlterField(
            model_name='westernmedicinediagnosis',
            name='belong',
            field=models.CharField(default=1, max_length=20, verbose_name='是谁的'),
        ),
    ]