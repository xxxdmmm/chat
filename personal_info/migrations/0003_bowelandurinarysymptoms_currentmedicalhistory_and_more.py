# Generated by Django 4.2 on 2024-06-21 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_info', '0002_alter_coldandhot_alvine_alter_coldandhot_foot_heart_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BowelAndUrinarySymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.IntegerField(blank=True, null=True, verbose_name='是谁的')),
                ('regular_bowel_movements', models.BooleanField(blank=True, null=True, verbose_name='大便全过程成形')),
                ('hard_start_soft_end', models.BooleanField(blank=True, null=True, verbose_name='开头硬结尾稀')),
                ('constipation', models.BooleanField(blank=True, null=True, verbose_name='大便干结')),
                ('difficult_to_pass', models.BooleanField(blank=True, null=True, verbose_name='大便难下')),
                ('loose_stools', models.BooleanField(blank=True, null=True, verbose_name='大便糖稀')),
                ('watery_diarrhea', models.BooleanField(blank=True, null=True, verbose_name='大便水泻')),
                ('bowel_movement_frequency', models.PositiveSmallIntegerField(blank=True, choices=[(1, '一天一次'), (2, '两天一次'), (3, '三天一次')], null=True, verbose_name='大便几天一次')),
                ('frequent_urination', models.BooleanField(blank=True, null=True, verbose_name='尿频')),
                ('urination_urgency', models.BooleanField(blank=True, null=True, verbose_name='尿急')),
                ('cloudy_urine', models.BooleanField(blank=True, null=True, verbose_name='尿浊')),
                ('red_urine', models.BooleanField(blank=True, null=True, verbose_name='尿赤')),
                ('hematuria', models.BooleanField(blank=True, null=True, verbose_name='血尿')),
                ('urination_pain', models.BooleanField(blank=True, null=True, verbose_name='尿痛')),
                ('cloudy_white', models.BooleanField(blank=True, null=True, verbose_name='尿白')),
                ('incontinence', models.BooleanField(blank=True, null=True, verbose_name='漏尿')),
                ('incomplete_emptying', models.BooleanField(blank=True, null=True, verbose_name='尿不尽')),
                ('nocturia', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='夜尿次数')),
                ('history_of_enuresis', models.BooleanField(blank=True, null=True, verbose_name='有尿床史')),
                ('additional_notes', models.TextField(blank=True, null=True, verbose_name='其他症状描述')),
            ],
        ),
        migrations.CreateModel(
            name='CurrentMedicalHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.IntegerField(blank=True, null=True, verbose_name='是谁的')),
                ('symptoms', models.TextField(blank=True, null=True, verbose_name='既往病史')),
            ],
        ),
        migrations.CreateModel(
            name='DietCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.IntegerField(blank=True, null=True, verbose_name='是谁的')),
                ('Abdominal_bloating', models.BooleanField(blank=True, null=True, verbose_name='腹胀')),
                ('Fullness_of_abdomen', models.BooleanField(blank=True, null=True, verbose_name='腹满')),
                ('celialgia', models.BooleanField(blank=True, null=True, verbose_name='腹痛')),
                ('Acid_regurgitation', models.BooleanField(blank=True, null=True, verbose_name='反酸')),
                ('nausea', models.BooleanField(blank=True, null=True, verbose_name='恶心')),
                ('vomit', models.BooleanField(blank=True, null=True, verbose_name='呕吐')),
                ('no_appetite', models.BooleanField(blank=True, null=True, verbose_name='无食欲')),
                ('overappetite', models.BooleanField(blank=True, null=True, verbose_name='胃口过大')),
                ('Tasteless', models.BooleanField(blank=True, null=True, verbose_name='食之无味')),
                ('dont_know_hungry', models.BooleanField(blank=True, null=True, verbose_name='到点不知道饿')),
                ('additional_notes', models.TextField(blank=True, null=True, verbose_name='其他症状描述')),
            ],
        ),
        migrations.CreateModel(
            name='GynecologicalSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.IntegerField(blank=True, null=True, verbose_name='是谁的')),
                ('dysmenorrhea', models.BooleanField(blank=True, null=True, verbose_name='痛经')),
                ('blood_clots_in_menses', models.BooleanField(blank=True, null=True, verbose_name='经有血块')),
                ('menstruation_advance', models.BooleanField(blank=True, null=True, verbose_name='月经提前')),
                ('menstruation_delay', models.BooleanField(blank=True, null=True, verbose_name='月经延后')),
                ('leukorrhea', models.BooleanField(blank=True, null=True, verbose_name='白带')),
                ('yellow_leukorrhea', models.BooleanField(blank=True, null=True, verbose_name='黄带')),
                ('red_leukorrhea', models.BooleanField(blank=True, null=True, verbose_name='赤带')),
                ('foul_smell', models.BooleanField(blank=True, null=True, verbose_name='气味腥臭')),
                ('vulvar_pruritus', models.BooleanField(blank=True, null=True, verbose_name='外阴瘙痒')),
                ('additional_notes', models.TextField(blank=True, null=True, verbose_name='其他症状描述')),
            ],
        ),
        migrations.CreateModel(
            name='NumbnessSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.IntegerField(blank=True, null=True, verbose_name='是谁的')),
                ('finger_stiff', models.BooleanField(blank=True, null=True, verbose_name='手指僵')),
                ('finger_numb', models.BooleanField(blank=True, null=True, verbose_name='手指麻')),
                ('upper_arm_numb', models.BooleanField(blank=True, null=True, verbose_name='胳膊无力')),
                ('upper_arm_stiff', models.BooleanField(blank=True, null=True, verbose_name='胳膊麻木')),
                ('toe_stiff', models.BooleanField(blank=True, null=True, verbose_name='脚趾僵')),
                ('toe_numb', models.BooleanField(blank=True, null=True, verbose_name='脚趾麻')),
                ('Aching_waist_aching_legs', models.BooleanField(blank=True, null=True, verbose_name='腰酸腿痛')),
                ('General_fatigue', models.BooleanField(blank=True, null=True, verbose_name='全身乏力')),
                ('lower_leg_weak', models.BooleanField(blank=True, null=True, verbose_name='腿没劲')),
                ('lower_leg_numb', models.BooleanField(blank=True, null=True, verbose_name='腿麻木')),
                ('calf_sore', models.BooleanField(blank=True, null=True, verbose_name='小腿酸痛')),
                ('wrist_numb', models.BooleanField(blank=True, null=True, verbose_name='手腕麻')),
                ('wrist_stiff', models.BooleanField(blank=True, null=True, verbose_name='手腕每')),
                ('ankle_numb', models.BooleanField(blank=True, null=True, verbose_name='足腕麻')),
                ('ankle_stiff', models.BooleanField(blank=True, null=True, verbose_name='足腕僵')),
                ('additional_notes', models.TextField(blank=True, null=True, verbose_name='其他症状描述')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.IntegerField(blank=True, null=True, verbose_name='是谁的')),
                ('symptom', models.TextField(blank=True, null=True, verbose_name='症状')),
                ('prescription', models.TextField(blank=True, null=True, verbose_name='处方')),
                ('additional_notes', models.TextField(blank=True, null=True, verbose_name='其他补充')),
            ],
        ),
        migrations.CreateModel(
            name='SleepDisorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.IntegerField(blank=True, null=True, verbose_name='是谁的')),
                ('difficulty_falling_asleep', models.BooleanField(blank=True, null=True, verbose_name='入睡困难')),
                ('light_sleep', models.BooleanField(blank=True, null=True, verbose_name='睡眠浅')),
                ('easy_awake', models.BooleanField(blank=True, null=True, verbose_name='易醒')),
                ('frequent_night_waking', models.BooleanField(blank=True, null=True, verbose_name='频繁夜醒')),
                ('dream_disturbed_sleep', models.BooleanField(blank=True, null=True, verbose_name='多梦')),
                ('wake_up_refreshed', models.BooleanField(blank=True, null=True, verbose_name='醒后难入睡')),
                ('body_hot', models.BooleanField(blank=True, null=True, verbose_name='全是燥热')),
                ('body_cold', models.BooleanField(blank=True, null=True, verbose_name='全是冰冷')),
                ('Ice_fever_of_lower_extremity', models.BooleanField(blank=True, null=True, verbose_name='下肢冰冷')),
                ('night_count', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='夜醒次数')),
                ('additional_notes', models.TextField(blank=True, null=True, verbose_name='其他症状描述')),
            ],
        ),
        migrations.CreateModel(
            name='Thirst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.IntegerField(blank=True, null=True, verbose_name='是谁的')),
                ('not_thirsty', models.BooleanField(blank=True, null=True, verbose_name='口不渴')),
                ('thirsty', models.BooleanField(blank=True, null=True, verbose_name='渴')),
                ('thirsty_but_not_wanting_to_drink', models.BooleanField(blank=True, null=True, verbose_name='渴不欲饮')),
                ('drink_hot_water', models.BooleanField(blank=True, null=True, verbose_name='想喝热水')),
                ('not_quenched_by_drinking', models.BooleanField(blank=True, null=True, verbose_name='千杯不解渴')),
                ('additional_notes', models.TextField(blank=True, null=True, verbose_name='其他症状描述')),
            ],
        ),
        migrations.CreateModel(
            name='TongueAppearance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.IntegerField(blank=True, null=True, verbose_name='是谁的')),
                ('Coated_tongue_white', models.BooleanField(blank=True, null=True, verbose_name='舌苔白')),
                ('Coated_tongue_yellow', models.BooleanField(blank=True, null=True, verbose_name='舌苔黄')),
                ('Coated_tongue_thick', models.BooleanField(blank=True, null=True, verbose_name='舌苔厚')),
                ('Coated_tongue_greasy', models.BooleanField(blank=True, null=True, verbose_name='舌苔腻')),
                ('Coated_tongue_slide', models.BooleanField(blank=True, null=True, verbose_name='舌苔滑')),
                ('Body_of_tongue_big', models.BooleanField(blank=True, null=True, verbose_name='舌体大')),
                ('Body_of_tongue_small', models.BooleanField(blank=True, null=True, verbose_name='舌体小')),
                ('Body_of_tongue_crack', models.BooleanField(blank=True, null=True, verbose_name='舌体有裂纹')),
                ('Tongue_color', models.SmallIntegerField(blank=True, choices=[(1, '红'), (2, '淡'), (3, '白'), (4, '灰'), (5, '紫'), (6, '黑')], null=True, verbose_name='舌色')),
                ('tongue_quality', models.SmallIntegerField(blank=True, choices=[(1, '干'), (2, '湿')], null=True, verbose_name='舌质')),
                ('additional_notes', models.TextField(blank=True, null=True, verbose_name='其他症状描述')),
            ],
        ),
        migrations.CreateModel(
            name='UrologicalSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.IntegerField(blank=True, null=True, verbose_name='是谁的')),
                ('impotence', models.BooleanField(blank=True, null=True, verbose_name='阳痿')),
                ('premature_ejaculation', models.BooleanField(blank=True, null=True, verbose_name='早泄')),
                ('nocturnal_emission', models.BooleanField(blank=True, null=True, verbose_name='遗精')),
                ('spermatorrhea', models.BooleanField(blank=True, null=True, verbose_name='滑精')),
                ('weak_erection', models.BooleanField(blank=True, null=True, verbose_name='举而不坚')),
                ('decreased_libido', models.BooleanField(blank=True, null=True, verbose_name='性欲减退')),
                ('damp_scrotum', models.BooleanField(blank=True, null=True, verbose_name='阴囊潮湿')),
                ('scrotal_pain', models.BooleanField(blank=True, null=True, verbose_name='阴囊疼痛')),
                ('scrotal_wetness_and_itching', models.BooleanField(blank=True, null=True, verbose_name='阴囊湿痒')),
                ('additional_notes', models.TextField(blank=True, null=True, verbose_name='其他症状描述')),
            ],
        ),
        migrations.CreateModel(
            name='WesternMedicineDiagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.IntegerField(blank=True, null=True, verbose_name='是谁的')),
                ('blood_pressure', models.CharField(blank=True, max_length=50, null=True, verbose_name='高血压')),
                ('hyperglycemia', models.CharField(blank=True, max_length=50, null=True, verbose_name='高血糖')),
                ('hyperlipidemia', models.CharField(blank=True, max_length=50, null=True, verbose_name='高血脂')),
                ('hyperuricemia', models.CharField(blank=True, max_length=50, null=True, verbose_name='高尿酸')),
                ('creatinine', models.CharField(blank=True, max_length=50, null=True, verbose_name='肌酐尿素值')),
                ('additional_notes', models.TextField(blank=True, null=True, verbose_name='其他症状描述')),
            ],
        ),
        migrations.AddField(
            model_name='coldandhot',
            name='additional_notes',
            field=models.TextField(blank=True, null=True, verbose_name='其他症状描述'),
        ),
        migrations.AddField(
            model_name='headnosemouth',
            name='additional_notes',
            field=models.TextField(blank=True, null=True, verbose_name='其他症状描述'),
        ),
        migrations.AddField(
            model_name='physicalstrength',
            name='additional_notes',
            field=models.TextField(blank=True, null=True, verbose_name='其他症状描述'),
        ),
        migrations.AlterField(
            model_name='headnosemouth',
            name='anosmia',
            field=models.BooleanField(blank=True, null=True, verbose_name='鼻不闻香臭'),
        ),
        migrations.AlterField(
            model_name='headnosemouth',
            name='bitter_taste',
            field=models.BooleanField(blank=True, null=True, verbose_name='口苦'),
        ),
        migrations.AlterField(
            model_name='headnosemouth',
            name='bland_taste',
            field=models.BooleanField(blank=True, null=True, verbose_name='口淡'),
        ),
        migrations.AlterField(
            model_name='headnosemouth',
            name='clear_discharge',
            field=models.BooleanField(blank=True, null=True, verbose_name='流清涕'),
        ),
        migrations.AlterField(
            model_name='headnosemouth',
            name='dizzy',
            field=models.BooleanField(blank=True, null=True, verbose_name='头晕'),
        ),
        migrations.AlterField(
            model_name='headnosemouth',
            name='dry_mouth',
            field=models.BooleanField(blank=True, null=True, verbose_name='口干'),
        ),
        migrations.AlterField(
            model_name='headnosemouth',
            name='dry_nose',
            field=models.BooleanField(blank=True, null=True, verbose_name='鼻干'),
        ),
        migrations.AlterField(
            model_name='headnosemouth',
            name='head_itch',
            field=models.BooleanField(blank=True, null=True, verbose_name='头痒'),
        ),
        migrations.AlterField(
            model_name='headnosemouth',
            name='headache',
            field=models.BooleanField(blank=True, null=True, verbose_name='头疼'),
        ),
        migrations.AlterField(
            model_name='headnosemouth',
            name='heavy_head',
            field=models.BooleanField(blank=True, null=True, verbose_name='头重'),
        ),
        migrations.AlterField(
            model_name='headnosemouth',
            name='nasal_congestion',
            field=models.BooleanField(blank=True, null=True, verbose_name='鼻塞'),
        ),
        migrations.AlterField(
            model_name='headnosemouth',
            name='nose_itch',
            field=models.BooleanField(blank=True, null=True, verbose_name='鼻痒'),
        ),
        migrations.AlterField(
            model_name='headnosemouth',
            name='nosebleed',
            field=models.BooleanField(blank=True, null=True, verbose_name='流鼻血'),
        ),
        migrations.AlterField(
            model_name='headnosemouth',
            name='swollen_gums',
            field=models.BooleanField(blank=True, null=True, verbose_name='牙龈肿痛'),
        ),
        migrations.AlterField(
            model_name='headnosemouth',
            name='thick_discharge',
            field=models.BooleanField(blank=True, null=True, verbose_name='流浊涕'),
        ),
        migrations.AlterField(
            model_name='headnosemouth',
            name='ulcers',
            field=models.BooleanField(blank=True, null=True, verbose_name='口腔溃疡'),
        ),
        migrations.AlterField(
            model_name='physicalstrength',
            name='Shortness',
            field=models.BooleanField(blank=True, null=True, verbose_name='气短难言'),
        ),
        migrations.AlterField(
            model_name='physicalstrength',
            name='fatigue_easily',
            field=models.BooleanField(blank=True, null=True, verbose_name='容易疲劳'),
        ),
        migrations.AlterField(
            model_name='physicalstrength',
            name='heavy_legs',
            field=models.BooleanField(blank=True, null=True, verbose_name='腿沉重'),
        ),
        migrations.AlterField(
            model_name='physicalstrength',
            name='weakness',
            field=models.BooleanField(blank=True, null=True, verbose_name='浑身无力'),
        ),
        migrations.AlterField(
            model_name='physicalstrength',
            name='weakness_legs',
            field=models.BooleanField(blank=True, null=True, verbose_name='腿无力'),
        ),
    ]
