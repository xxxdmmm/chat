# Generated by Django 4.2 on 2024-07-26 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_info_new', '0003_howmangbig_howmangsmall_hownightawake_hownightsleep_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('windAndCold', models.BooleanField(default=False, verbose_name='您感觉怕风怕冷的情况？')),
                ('heatSymptoms', models.BooleanField(default=False, verbose_name='您身体的某个部位经常感觉发热的情况？')),
                ('coldSymptoms', models.BooleanField(default=False, verbose_name='您身体的某个部位经常冰凉的情况？')),
                ('sweatingSymptoms', models.BooleanField(default=False, verbose_name='您平时的出汗情况？')),
                ('bowelAndFlatulenceSymptoms', models.BooleanField(default=False, verbose_name='大便及排气情况？')),
                ('urinationSymptoms', models.BooleanField(default=False, verbose_name='小便情况？')),
                ('hydrationSymptoms', models.BooleanField(default=False, verbose_name='您的饮水情况？')),
                ('dietSymptoms', models.BooleanField(default=False, verbose_name='您的饮食情况？')),
                ('coughSymptoms', models.BooleanField(default=False, verbose_name='您咳嗽吐痰的情况？')),
                ('emotionalSymptoms', models.BooleanField(default=False, verbose_name='您的情绪情况？')),
                ('facialSymptoms', models.BooleanField(default=False, verbose_name='五官？')),
                ('sleepSymptoms', models.BooleanField(default=False, verbose_name='睡眠情况？')),
                ('painSymptoms', models.BooleanField(default=False, verbose_name='有无疼痛感觉（痛的部位）？')),
                ('oralSymptoms', models.BooleanField(default=False, verbose_name='口中感受？')),
                ('physicalSymptoms', models.BooleanField(default=False, verbose_name='体力情况？')),
                ('bleedingSymptoms', models.BooleanField(default=False, verbose_name='出血情况？')),
                ('habitSymptoms', models.BooleanField(default=False, verbose_name='习惯？')),
                ('howMangBig', models.BooleanField(default=False, verbose_name='大便一天几次？')),
                ('howNightSleep', models.BooleanField(default=False, verbose_name='夜间几点钟睡？')),
                ('howNightAwake', models.BooleanField(default=False, verbose_name='夜间醒在几点钟？')),
                ('howMangSmall', models.BooleanField(default=False, verbose_name='一夜排尿几次？（夜尿情况）')),
            ],
        ),
        migrations.AlterField(
            model_name='howmangbig',
            name='bowel_movements_frequency',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='大便一天几次？'),
        ),
        migrations.AlterField(
            model_name='howmangsmall',
            name='nocturia_frequency',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='一夜排尿几次？（夜尿情况）'),
        ),
        migrations.AlterField(
            model_name='hownightawake',
            name='wake_up_time_at_night',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='夜间醒在几点钟？'),
        ),
        migrations.AlterField(
            model_name='hownightsleep',
            name='sleep_time_at_night',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='夜间几点钟睡？'),
        ),
    ]