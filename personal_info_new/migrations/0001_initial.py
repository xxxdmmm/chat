# Generated by Django 4.2 on 2024-07-25 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BleedingSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('bleeding_gums', models.BooleanField(default=False, verbose_name='刷牙出血')),
                ('spontaneous_oral_bleeding', models.BooleanField(default=False, verbose_name='口腔自然出血')),
                ('bleeding_from_ears', models.BooleanField(default=False, verbose_name='耳朵出血')),
                ('bright_red_stools', models.BooleanField(default=False, verbose_name='大便出血，鲜红色')),
                ('dark_red_stools', models.BooleanField(default=False, verbose_name='大便出血暗红色')),
                ('hemorrhoids_bleeding', models.BooleanField(default=False, verbose_name='痔疮出血')),
                ('hematuria', models.BooleanField(default=False, verbose_name='尿血')),
                ('no_symptoms', models.BooleanField(default=False, verbose_name='无以上症状')),
            ],
        ),
        migrations.CreateModel(
            name='BowelAndFlatulenceSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('watery_stools', models.BooleanField(default=False, verbose_name='水泻，吃什么拉什么')),
                ('diarrhea', models.BooleanField(default=False, verbose_name='滤稀（如塘鸡屎一样）')),
                ('loose_stools', models.BooleanField(default=False, verbose_name='稀软')),
                ('formed_stools', models.BooleanField(default=False, verbose_name='成形')),
                ('smooth_bowel_movements', models.BooleanField(default=False, verbose_name='顺畅')),
                ('hard_stools', models.BooleanField(default=False, verbose_name='干硬')),
                ('hard_start_soft_end', models.BooleanField(default=False, verbose_name='开头硬，后尾软、稀、滤')),
                ('unsatisfied', models.BooleanField(default=False, verbose_name='不爽、下坠')),
                ('sticky_stools', models.BooleanField(default=False, verbose_name='大便易粘马桶，难冲洗')),
                ('foul_smell_farts', models.BooleanField(default=False, verbose_name='放臭屁，气味如臭鸡蛋')),
                ('difficult_bowel_movements', models.BooleanField(default=False, verbose_name='大便困难')),
                ('pellet_stools', models.BooleanField(default=False, verbose_name='如羊屎个一样')),
                ('rarely_pass_gas', models.BooleanField(default=False, verbose_name='极少放屁')),
                ('non_foul_smell_farts', models.BooleanField(default=False, verbose_name='放屁不臭')),
                ('excessive_pass_gas', models.BooleanField(default=False, verbose_name='放屁多，但不臭')),
                ('cough_induces_flatulence', models.BooleanField(default=False, verbose_name='咳嗽伴有屁出来')),
                ('urine_leak_when_coughing', models.BooleanField(default=False, verbose_name='咳嗽尿出来')),
                ('urine_leak_when_laughing', models.BooleanField(default=False, verbose_name='笑时尿会出来')),
                ('urine_overflow_inaudibly', models.BooleanField(default=False, verbose_name='听到水声就想尿出来')),
                ('no_symptoms', models.BooleanField(default=False, verbose_name='无以上症状')),
            ],
        ),
        migrations.CreateModel(
            name='ColdSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('cold_hands_and_feet', models.BooleanField(default=False, verbose_name='经常手脚冰凉')),
                ('cold_back', models.BooleanField(default=False, verbose_name='经常背心冰凉')),
                ('cold_abdomen', models.BooleanField(default=False, verbose_name='经常腹部冰凉')),
                ('cold_waist', models.BooleanField(default=False, verbose_name='经常腰部冰凉')),
                ('cold_whole_body', models.BooleanField(default=False, verbose_name='经常全身冰凉')),
                ('cold_lower_limbs', models.BooleanField(default=False, verbose_name='双下肢冰凉')),
                ('cold_half_body', models.BooleanField(default=False, verbose_name='半边身体冰凉')),
                ('cold_neck', models.BooleanField(default=False, verbose_name='颈脖发凉，需要带上围巾')),
                ('cold_wrist_to_fingers', models.BooleanField(default=False, verbose_name='手腕到手指冰凉，不敢沾自来水')),
                ('cold_chest_to_throat', models.BooleanField(default=False, verbose_name='心口窝至喉咙冰凉，不敢穿低领衣服')),
                ('cold_toes', models.BooleanField(default=False, verbose_name='脚趾头凉')),
                ('cold_below_knee', models.BooleanField(default=False, verbose_name='膝盖以下冰凉')),
                ('cold_below_calf', models.BooleanField(default=False, verbose_name='小腿肚子以下冰凉')),
                ('cold_arms', models.BooleanField(default=False, verbose_name='胳膊凉')),
                ('cold_shoulders', models.BooleanField(default=False, verbose_name='肩膀头凉')),
                ('stiff_fingers_upon_waking', models.BooleanField(default=False, verbose_name='早上醒来手指头僵')),
                ('numb_hands', models.BooleanField(default=False, verbose_name='手麻木')),
                ('stiff_hands_upon_waking', models.BooleanField(default=False, verbose_name='早上醒来手僵的捏不成拳头')),
                ('numb_legs', models.BooleanField(default=False, verbose_name='腿麻木')),
                ('no_cold_symptoms', models.BooleanField(default=False, verbose_name='无以上症状')),
            ],
        ),
        migrations.CreateModel(
            name='CoughSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('cough_no_phlegm', models.BooleanField(default=False, verbose_name='咳嗽无痰')),
                ('cough_yellow_phlegm', models.BooleanField(default=False, verbose_name='咳嗽吐黄痰')),
                ('cough_white_phlegm', models.BooleanField(default=False, verbose_name='咳嗽吐白痰')),
                ('cough_thin_clear_phlegm', models.BooleanField(default=False, verbose_name='咳嗽吐清稀痰')),
                ('spit_sputum_not_coughing', models.BooleanField(default=False, verbose_name='不咳嗽但吐涎痰、白沫痰')),
                ('no_symptoms', models.BooleanField(default=False, verbose_name='无以上症状')),
            ],
        ),
        migrations.CreateModel(
            name='DietSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('likes_alcohol', models.BooleanField(default=False, verbose_name='爱喝酒')),
                ('likes_meat', models.BooleanField(default=False, verbose_name='爱吃肉')),
                ('likes_night_snacks', models.BooleanField(default=False, verbose_name='爱吃夜宵')),
                ('likes_vegetarian', models.BooleanField(default=False, verbose_name='爱吃素')),
                ('needs_full_stomach_or_drunk_to_sleep', models.BooleanField(default=False, verbose_name='吃饱、喝醉了才睡的着觉')),
                ('prefers_cold_food', models.BooleanField(default=False, verbose_name='喜生冷食物')),
                ('prefers_hot_food', models.BooleanField(default=False, verbose_name='喜温热食物')),
                ('always_feels_hungry', models.BooleanField(default=False, verbose_name='总感到饥饿，吃的多，拉的多')),
                ('feels_full_easily', models.BooleanField(default=False, verbose_name='吃一点点就饱了，放下碗一会就饿了')),
                ('no_appetite_at_meal_time', models.BooleanField(default=False, verbose_name='到饭点了不知道饿、没胃口')),
                ('frequent_bloating_nausea', models.BooleanField(default=False, verbose_name='经常腹胀及反胃')),
                ('prefers_soft_food', models.BooleanField(default=False, verbose_name='喜稀软食物')),
                ('prefers_dry_food', models.BooleanField(default=False, verbose_name='喜干燥食物')),
                ('prefers_sweet', models.BooleanField(default=False, verbose_name='喜甜食')),
                ('prefers_sour', models.BooleanField(default=False, verbose_name='喜酸')),
                ('prefers_spicy', models.BooleanField(default=False, verbose_name='喜辣')),
                ('prefers_salty', models.BooleanField(default=False, verbose_name='喜咸')),
                ('burps_Occasionally', models.BooleanField(default=False, verbose_name='时而打隔')),
                ('frequent_burping', models.BooleanField(default=False, verbose_name='经常打隔')),
                ('series_of_burps', models.BooleanField(default=False, verbose_name='打隔成串')),
                ('bland_taste', models.BooleanField(default=False, verbose_name='口味淡，吃啥美食都不香')),
                ('no_symptoms', models.BooleanField(default=False, verbose_name='无以上症状')),
            ],
        ),
        migrations.CreateModel(
            name='EmotionalSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('easily_angry', models.BooleanField(default=False, verbose_name='经常容易生气')),
                ('decreased_boldness', models.BooleanField(default=False, verbose_name='没有过去胆子大')),
                ('loves_scolding', models.BooleanField(default=False, verbose_name='爱骂人')),
                ('feels_hateful', models.BooleanField(default=False, verbose_name='总觉得在恨谁一样，但实际上谁也不恨')),
                ('timid', models.BooleanField(default=False, verbose_name='胆小，不敢一个人待在一个地方')),
                ('loves_smashing_objects', models.BooleanField(default=False, verbose_name='爱打砸物件')),
                ('paranoid_behind', models.BooleanField(default=False, verbose_name='时时向身后看，总觉得身后有人要抓捕自己')),
                ('feels_gossiped', models.BooleanField(default=False, verbose_name='总觉得别人再说自己坏话')),
                ('feels_plotted_against', models.BooleanField(default=False, verbose_name='总觉得有人要谋害自己')),
                ('loves_solitude', models.BooleanField(default=False, verbose_name='喜欢一个人关门独处')),
                ('secretly_laughing', models.BooleanField(default=False, verbose_name='一人人偷偷地笑')),
                ('explosive_temper', models.BooleanField(default=False, verbose_name='爱暴跳如雷')),
                ('restless_night', models.BooleanField(default=False, verbose_name='夜晚不睡觉爱折腾')),
                ('loves_climbing_and_shouting', models.BooleanField(default=False, verbose_name='爱登高喊叫、唱歌')),
                ('no_symptoms', models.BooleanField(default=False, verbose_name='无以上症状')),
            ],
        ),
        migrations.CreateModel(
            name='FacialSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('nasal_congestion', models.BooleanField(default=False, verbose_name='鼻塞')),
                ('nasal_coolness', models.BooleanField(default=False, verbose_name='鼻子冒凉气')),
                ('nasal_heat', models.BooleanField(default=False, verbose_name='鼻子冒热气')),
                ('decreased_smell', models.BooleanField(default=False, verbose_name='嗅觉下降')),
                ('anosmia', models.BooleanField(default=False, verbose_name='闻不到香臭')),
                ('persistent_throat_dryness', models.BooleanField(default=False, verbose_name='喉咙持续干燥')),
                ('dryness_causing_midnight_drink', models.BooleanField(default=False, verbose_name='半夜时咽干起床喝水')),
                ('throat_itching', models.BooleanField(default=False, verbose_name='喉咙痒')),
                ('foreign_body_sensation_in_throat', models.BooleanField(default=False, verbose_name='喉咙有异物感')),
                ('dry_eyes', models.BooleanField(default=False, verbose_name='眼睛干涩')),
                ('swollen_eyes', models.BooleanField(default=False, verbose_name='眼睛红肿')),
                ('itching_eyes', models.BooleanField(default=False, verbose_name='眼睛干痒')),
                ('blurred_vision', models.BooleanField(default=False, verbose_name='眼睛看东西模糊')),
                ('tearing_in_wind', models.BooleanField(default=False, verbose_name='眼睛迎风流泪')),
                ('eyes_sensitive_to_wind_and_cold', models.BooleanField(default=False, verbose_name='眼睛怕风怕冷')),
                ('unconscious_tearing', models.BooleanField(default=False, verbose_name='泪流出来时自己没感觉到')),
                ('eyelid_itching_and_ulceration', models.BooleanField(default=False, verbose_name='眼衔痒烂')),
                ('inverted_eyelashes', models.BooleanField(default=False, verbose_name='爱倒睫毛')),
                ('hearing_loss', models.BooleanField(default=False, verbose_name='听力减退')),
                ('deafness', models.BooleanField(default=False, verbose_name='耳聋')),
                ('tinnitus', models.BooleanField(default=False, verbose_name='耳鸣')),
                ('ear_pain', models.BooleanField(default=False, verbose_name='耳痛')),
                ('itchy_ears', models.BooleanField(default=False, verbose_name='耳痒但掏不到，不知哪里痒')),
                ('discharge_with_odor', models.BooleanField(default=False, verbose_name='耳中时常有渗出液，有异味')),
                ('weak_teeth_while_chewing', models.BooleanField(default=False, verbose_name='咬嚼食物牙没有力气')),
                ('teeth_sensitive_to_cold', models.BooleanField(default=False, verbose_name='牙不敢沾凉水')),
                ('teeth_sensitive_to_hot', models.BooleanField(default=False, verbose_name='牙不敢沾热水')),
                ('sensitive_teeth_to_cold', models.BooleanField(default=False, verbose_name='牙齿怕冷')),
                ('toothache_from_cold_water', models.BooleanField(default=False, verbose_name='凉水漱口牙就痛')),
                ('choking_while_drinking', models.BooleanField(default=False, verbose_name='喝水时爱呛到')),
                ('no_symptoms', models.BooleanField(default=False, verbose_name='无以上症状')),
            ],
        ),
        migrations.CreateModel(
            name='HabitSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('sleeps_shirts_off', models.BooleanField(default=False, verbose_name='爱光膀子睡觉')),
                ('sleeps_with_arms_outside', models.BooleanField(default=False, verbose_name='爱胳膊放在被子外睡觉')),
                ('sleeps_with_legs_outside', models.BooleanField(default=False, verbose_name='爱腿脚放在被子外睡觉')),
                ('sleeps_with_window_open', models.BooleanField(default=False, verbose_name='爱开着窗户吹风睡觉')),
                ('sleeps_with_air_conditioner_or_fan', models.BooleanField(default=False, verbose_name='爱空调或风扇对着吹才舒服')),
                ('no_symptoms', models.BooleanField(default=False, verbose_name='无以上症状')),
            ],
        ),
        migrations.CreateModel(
            name='HeatSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('head_heat', models.BooleanField(default=False, verbose_name='头发热')),
                ('face_heat', models.BooleanField(default=False, verbose_name='脸部发热')),
                ('chest_and_back_heat', models.BooleanField(default=False, verbose_name='前后背心发热')),
                ('palms_and_soles_heat', models.BooleanField(default=False, verbose_name='手脚心发热')),
                ('afternoon_heat', models.BooleanField(default=False, verbose_name='中午以后发热')),
                ('evening_heat', models.BooleanField(default=False, verbose_name='入夜以后发热')),
                ('no_heat_symptoms', models.BooleanField(default=False, verbose_name='无以上症状')),
            ],
        ),
        migrations.CreateModel(
            name='HydrationSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('likes_cold_water', models.BooleanField(default=False, verbose_name='喜欢喝冷水')),
                ('likes_hot_water', models.BooleanField(default=False, verbose_name='喜欢喝热水')),
                ('does_not_feel_thirsty', models.BooleanField(default=False, verbose_name='口不渴')),
                ('dry_mouth_dislikes_water', models.BooleanField(default=False, verbose_name='口干，但不喜欢喝水')),
                ('thirsty_no_matter_how_much_drink', models.BooleanField(default=False, verbose_name='口渴，喝多少都不解渴')),
                ('no_symptoms', models.BooleanField(default=False, verbose_name='无以上症状')),
            ],
        ),
        migrations.CreateModel(
            name='OralSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('bad_breath', models.BooleanField(default=False, verbose_name='口臭')),
                ('sticky_mouth', models.BooleanField(default=False, verbose_name='口中粘涎')),
                ('stringy_saliva', models.BooleanField(default=False, verbose_name='张口粘涎扯线')),
                ('sweet_taste', models.BooleanField(default=False, verbose_name='口甜')),
                ('watery_saliva', models.BooleanField(default=False, verbose_name='口中清涎，张口即可流出来')),
                ('tasteless', models.BooleanField(default=False, verbose_name='口淡乏味')),
                ('morning_bitterness', models.BooleanField(default=False, verbose_name='晨起口苦')),
                ('midnight_bitterness', models.BooleanField(default=False, verbose_name='半夜口苦')),
                ('all_day_bitterness', models.BooleanField(default=False, verbose_name='全天口苦')),
                ('salty_taste', models.BooleanField(default=False, verbose_name='口咸')),
                ('abdominal_distension', models.BooleanField(default=False, verbose_name='口腥')),
                ('dry_mouth', models.BooleanField(default=False, verbose_name='口干')),
                ('mouth_ulcers', models.BooleanField(default=False, verbose_name='口腔溃疡')),
                ('peeling_lips', models.BooleanField(default=False, verbose_name='口唇起皮，起硬壳')),
                ('no_symptoms', models.BooleanField(default=False, verbose_name='无以上症状')),
            ],
        ),
        migrations.CreateModel(
            name='OtherSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('bowel_movements_frequency', models.CharField(blank=True, max_length=20, null=True, verbose_name='大便天一次？')),
                ('sleep_time_at_night', models.CharField(blank=True, max_length=20, null=True, verbose_name='夜间点钟睡？')),
                ('wake_up_time_at_night', models.CharField(blank=True, max_length=20, null=True, verbose_name='夜间醒在点钟？')),
                ('nocturia_frequency', models.CharField(blank=True, max_length=20, null=True, verbose_name='一夜排尿次？（夜尿情况）')),
            ],
        ),
        migrations.CreateModel(
            name='PainSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('toothache', models.BooleanField(default=False, verbose_name='牙痛')),
                ('headache', models.BooleanField(default=False, verbose_name='头痛')),
                ('dizzy', models.BooleanField(default=False, verbose_name='头晕')),
                ('head_yun', models.BooleanField(default=False, verbose_name='头眩晕')),
                ('shoulder_pain', models.BooleanField(default=False, verbose_name='肩膀痛')),
                ('back_pain', models.BooleanField(default=False, verbose_name='背心痛')),
                ('waist_pain', models.BooleanField(default=False, verbose_name='腰疼')),
                ('limb_joint_pain', models.BooleanField(default=False, verbose_name='四肢关节疼')),
                ('general_body_pain', models.BooleanField(default=False, verbose_name='浑身疼')),
                ('knee_pain', models.BooleanField(default=False, verbose_name='膝盖疼')),
                ('leg_pain_up', models.BooleanField(default=False, verbose_name='上坎腿疼')),
                ('leg_pain_down', models.BooleanField(default=False, verbose_name='下坎腿疼')),
                ('occasional_leg_cramp', models.BooleanField(default=False, verbose_name='偶尔腿上有根经扯住了疼')),
                ('left_rib_pain', models.BooleanField(default=False, verbose_name='左肋骨疼')),
                ('right_rib_pain', models.BooleanField(default=False, verbose_name='右肋骨疼')),
                ('double_rib_pain', models.BooleanField(default=False, verbose_name='双肋骨痛')),
                ('double_rib_distension', models.BooleanField(default=False, verbose_name='双肋闷胀')),
                ('chest_pit_pain', models.BooleanField(default=False, verbose_name='心口窝疼')),
                ('pain_refusal_to_touch', models.BooleanField(default=False, verbose_name='痛的部位拒按，碰不得')),
                ('pain_like_pressure', models.BooleanField(default=False, verbose_name='痛喜按')),
                ('distension_pain_on_pressure', models.BooleanField(default=False, verbose_name='胀，按了痛')),
                ('distension_without_pain_on_pressure', models.BooleanField(default=False, verbose_name='胀闷，按了不痛')),
                ('fixed_pain', models.BooleanField(default=False, verbose_name='固定痛')),
                ('migratory_pain', models.BooleanField(default=False, verbose_name='走窜痛')),
                ('forehead_pain', models.BooleanField(default=False, verbose_name='额头痛')),
                ('top_of_head_pain', models.BooleanField(default=False, verbose_name='头顶痛')),
                ('temporal_headache', models.BooleanField(default=False, verbose_name='偏头痛')),
                ('back_of_head_pain', models.BooleanField(default=False, verbose_name='后脑勺痛')),
                ('no_symptoms', models.BooleanField(default=False, verbose_name='无以上症状')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('fatigue_and_tiredness', models.BooleanField(default=False, verbose_name='乏力困倦')),
                ('heavy_limbs_and_weak_legs', models.BooleanField(default=False, verbose_name='四肢沉重，腿没有劲')),
                ('easily_fatigued', models.BooleanField(default=False, verbose_name='容易疲劳')),
                ('shortness_of_breath_with_activity', models.BooleanField(default=False, verbose_name='稍作活动则喘气、出粗气')),
                ('lack_of_previous_diligence', models.BooleanField(default=False, verbose_name='没有过去勤快')),
                ('no_symptoms', models.BooleanField(default=False, verbose_name='无以上症状')),
            ],
        ),
        migrations.CreateModel(
            name='SleepSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('difficulty_falling_asleep', models.BooleanField(default=False, verbose_name='入睡困难')),
                ('has_manyDreams', models.BooleanField(default=False, verbose_name='多梦')),
                ('occasionalDreams', models.BooleanField(default=False, verbose_name='偶尔做梦')),
                ('poorDreamMemory', models.BooleanField(default=False, verbose_name='醒后梦记不清楚')),
                ('easy_to_wake_up', models.BooleanField(default=False, verbose_name='睡着了易醒')),
                ('difficulty_returning_to_sleep', models.BooleanField(default=False, verbose_name='醒后再难入睡')),
                ('mixed_dreams', models.BooleanField(default=False, verbose_name='各种梦错杂')),
                ('frequent_nightmare_wake_up', models.BooleanField(default=False, verbose_name='梦，时常会从梦中惊醒')),
                ('frequently_startled_awake', models.BooleanField(default=False, verbose_name='时时惊醒')),
                ('always_tired', models.BooleanField(default=False, verbose_name='嗑睡多，总觉得睡不够')),
                ('no_symptoms', models.BooleanField(default=False, verbose_name='无以上症状')),
            ],
        ),
        migrations.CreateModel(
            name='SweatingSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('spontaneous_sweat', models.BooleanField(default=False, verbose_name='好出汗（自汗）')),
                ('head_sweat', models.BooleanField(default=False, verbose_name='头出汗')),
                ('palm_and_sole_sweat', models.BooleanField(default=False, verbose_name='手足心出汗')),
                ('upper_body_sweat', models.BooleanField(default=False, verbose_name='上半身（裤腰带以上）出汗')),
                ('neck_sweat', models.BooleanField(default=False, verbose_name='颈脖爱出汗')),
                ('back_and_chest_sweat', models.BooleanField(default=False, verbose_name='后背心、前胸好出汗')),
                ('lower_body_no_sweat', models.BooleanField(default=False, verbose_name='裤腰带以下无汗')),
                ('night_sweat', models.BooleanField(default=False, verbose_name='睡着了出汗，醒了就无汗（盗汗）')),
                ('hot_flashes_sweat', models.BooleanField(default=False, verbose_name='经常身上一阵发热，就出汗（潮热）')),
                ('no_sweating_symptoms', models.BooleanField(default=False, verbose_name='无以上症状')),
            ],
        ),
        migrations.CreateModel(
            name='UrinationSymptoms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('small_amount_strong_smell', models.BooleanField(default=False, verbose_name='量少色黄，气味浓烈')),
                ('incomplete_emptying', models.BooleanField(default=False, verbose_name='尿不尽')),
                ('frequent_urination', models.BooleanField(default=False, verbose_name='尿频')),
                ('pale_color_odourless', models.BooleanField(default=False, verbose_name='小便色淡，清如自来水，无气味')),
                ('weak_urination_stream', models.BooleanField(default=False, verbose_name='排尿没有以前有力量')),
                ('morning_erection', models.BooleanField(default=False, verbose_name='有晨勃（男性必填）')),
                ('weak_urination_stream_no_force', models.BooleanField(default=False, verbose_name='排尿时是流下来没有任何力量')),
                ('no_morning_erection', models.BooleanField(default=False, verbose_name='无晨勃（男性必填）')),
                ('no_symptoms', models.BooleanField(default=False, verbose_name='无以上症状')),
            ],
        ),
        migrations.CreateModel(
            name='WindAndCold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('belong', models.CharField(max_length=20, verbose_name='是谁的')),
                ('very_fear_wind', models.BooleanField(default=False, verbose_name='特别怕风')),
                ('very_fear_cold', models.BooleanField(default=False, verbose_name='特别怕冷')),
                ('fear_wind', models.BooleanField(default=False, verbose_name='怕风')),
                ('fear_cold', models.BooleanField(default=False, verbose_name='怕冷')),
                ('hands_not_warm', models.BooleanField(default=False, verbose_name='双手不暖和')),
                ('feet_not_warm', models.BooleanField(default=False, verbose_name='双脚不暖和')),
                ('hands_and_feet_not_warn', models.BooleanField(default=False, verbose_name='手脚都不暖和')),
                ('no_symptom', models.BooleanField(default=False, verbose_name='特别怕冷')),
            ],
        ),
    ]