from django.db import models
from loginAndRegister.models import userInfo


# Create your models here.

class ColdAndHot(models.Model):
    belong = models.CharField(verbose_name="是谁的", max_length=20)
    tem_choices = (
        (1, "冷"),
        (2, "热"),
    )
    hand = models.SmallIntegerField(verbose_name="手", choices=tem_choices, blank=True, null=True)
    elbow = models.SmallIntegerField(verbose_name="肘", choices=tem_choices, blank=True, null=True)
    palm = models.SmallIntegerField(verbose_name="手心", choices=tem_choices, blank=True, null=True)
    prothorax = models.SmallIntegerField(verbose_name="前胸背心", choices=tem_choices, blank=True, null=True)
    Lumbosacral = models.SmallIntegerField(verbose_name="腰骶", choices=tem_choices, blank=True, null=True)
    foot = models.SmallIntegerField(verbose_name="足", choices=tem_choices, blank=True, null=True)
    Knee = models.SmallIntegerField(verbose_name="膝", choices=tem_choices, blank=True, null=True)
    Foot_heart = models.SmallIntegerField(verbose_name="足心", choices=tem_choices, blank=True, null=True)
    body = models.SmallIntegerField(verbose_name="身体", choices=tem_choices, blank=True, null=True)
    Alvine = models.SmallIntegerField(verbose_name="小腹", choices=tem_choices, blank=True, null=True)
    # 其他相关信息
    additional_notes = models.TextField(
        verbose_name="其他症状描述", blank=True, null=True)
    change_notes = models.TextField(
        verbose_name="本次信息的修改说明", blank=True, null=True)


class Sweat(models.Model):
    belong = models.CharField(verbose_name="是谁的", max_length=20)
    sweat_choices = (
        (1, "无"),
        (2, "有"),
    )
    spontaneous_sweat = models.SmallIntegerField(
        verbose_name="自汗", choices=sweat_choices, blank=True, null=True)
    night_sweat = models.SmallIntegerField(
        verbose_name="盗汗", choices=sweat_choices, blank=True, null=True)
    hot_flashes = models.SmallIntegerField(
        verbose_name="潮热汗", choices=sweat_choices, blank=True, null=True)
    chest_sweat = models.SmallIntegerField(
        verbose_name="前胸汗", choices=sweat_choices, blank=True, null=True)
    back_sweat = models.SmallIntegerField(
        verbose_name="背心汗", choices=sweat_choices, blank=True, null=True)

    other_sweat = models.TextField(null=True, blank=True, verbose_name="其他")
    change_notes = models.TextField(
        verbose_name="本次信息的修改说明", blank=True, null=True)


class HeadNoseMouth(models.Model):
    belong = models.CharField(verbose_name="是谁的", max_length=20)
    # 头部症状
    headache = models.BooleanField(verbose_name="头疼", blank=True, null=True)
    head_itch = models.BooleanField(verbose_name="头痒", blank=True, null=True)
    dizzy = models.BooleanField(verbose_name="头晕", blank=True, null=True)
    heavy_head = models.BooleanField(verbose_name="头重", blank=True, null=True)

    # 鼻子症状
    nasal_congestion = models.BooleanField(verbose_name="鼻塞", blank=True, null=True)
    nose_itch = models.BooleanField(verbose_name="鼻痒", blank=True, null=True)
    dry_nose = models.BooleanField(verbose_name="鼻干", blank=True, null=True)
    clear_discharge = models.BooleanField(verbose_name="流清涕", blank=True, null=True)
    thick_discharge = models.BooleanField(verbose_name="流浊涕", blank=True, null=True)
    nosebleed = models.BooleanField(verbose_name="流鼻血", blank=True, null=True)
    anosmia = models.BooleanField(verbose_name="鼻不闻香臭", blank=True, null=True)

    # 口腔症状
    dry_mouth = models.BooleanField(verbose_name="口干", blank=True, null=True)
    bitter_taste = models.BooleanField(verbose_name="口苦", blank=True, null=True)
    bland_taste = models.BooleanField(verbose_name="口淡", blank=True, null=True)
    ulcers = models.BooleanField(verbose_name="口腔溃疡", blank=True, null=True)
    swollen_gums = models.BooleanField(verbose_name="牙龈肿痛", blank=True, null=True)
    # 其他相关信息
    additional_notes = models.TextField(
        verbose_name="其他症状描述", blank=True, null=True)
    change_notes = models.TextField(
        verbose_name="本次信息的修改说明", blank=True, null=True)


class PhysicalStrength(models.Model):
    belong = models.CharField(verbose_name="是谁的", max_length=20)
    Shortness = models.BooleanField(verbose_name="气短难言", blank=True, null=True)
    fatigue_easily = models.BooleanField(verbose_name="容易疲劳", blank=True, null=True)
    heavy_legs = models.BooleanField(verbose_name="腿沉重", blank=True, null=True)
    weakness_legs = models.BooleanField(verbose_name="腿无力", blank=True, null=True)
    weakness = models.BooleanField(verbose_name="浑身无力", blank=True, null=True)
    # 其他相关信息
    additional_notes = models.TextField(
        verbose_name="其他症状描述", blank=True, null=True)
    change_notes = models.TextField(
        verbose_name="本次信息的修改说明", blank=True, null=True)


class SleepDisorder(models.Model):
    belong = models.CharField(verbose_name="是谁的", max_length=20)
    # 睡眠问题
    difficulty_falling_asleep = models.BooleanField(
        verbose_name="入睡困难", blank=True, null=True)
    light_sleep = models.BooleanField(
        verbose_name="睡眠浅", blank=True, null=True)
    easy_awake = models.BooleanField(
        verbose_name="易醒", blank=True, null=True)
    frequent_night_waking = models.BooleanField(
        verbose_name="频繁夜醒", blank=True, null=True)
    dream_disturbed_sleep = models.BooleanField(
        verbose_name="多梦", blank=True, null=True)
    wake_up_refreshed = models.BooleanField(
        verbose_name="醒后难入睡", blank=True, null=True)
    body_hot = models.BooleanField(
        verbose_name="全身燥热", blank=True, null=True)
    body_cold = models.BooleanField(
        verbose_name="全身冰冷", blank=True, null=True)
    Ice_fever_of_lower_extremity = models.BooleanField(
        verbose_name="下肢冰冷", blank=True, null=True)

    # 夜醒次数
    night_count = models.PositiveSmallIntegerField(
        verbose_name="夜醒次数", blank=True, null=True)

    # 其他相关信息
    additional_notes = models.TextField(
        verbose_name="其他症状描述", blank=True, null=True)
    change_notes = models.TextField(
        verbose_name="本次信息的修改说明", blank=True, null=True)


class DietCondition(models.Model):
    belong = models.CharField(verbose_name="是谁的", max_length=20)

    Abdominal_bloating = models.BooleanField(
        verbose_name="腹胀", blank=True, null=True)
    Fullness_of_abdomen = models.BooleanField(
        verbose_name="腹满", blank=True, null=True)
    celialgia = models.BooleanField(
        verbose_name="腹痛", blank=True, null=True)
    Acid_regurgitation = models.BooleanField(
        verbose_name="反酸", blank=True, null=True)
    nausea = models.BooleanField(
        verbose_name="恶心", blank=True, null=True)
    vomit = models.BooleanField(
        verbose_name="呕吐", blank=True, null=True)
    no_appetite = models.BooleanField(
        verbose_name="无食欲", blank=True, null=True)
    overappetite = models.BooleanField(
        verbose_name="胃口过大", blank=True, null=True)
    Tasteless = models.BooleanField(
        verbose_name="食之无味", blank=True, null=True)
    dont_know_hungry = models.BooleanField(
        verbose_name="到点不知道饿", blank=True, null=True)
    # 其他相关信息
    additional_notes = models.TextField(
        verbose_name="其他症状描述", blank=True, null=True)
    change_notes = models.TextField(
        verbose_name="本次信息的修改说明", blank=True, null=True)


class Thirst(models.Model):
    belong = models.CharField(verbose_name="是谁的", max_length=20)
    # 口渴症状
    not_thirsty = models.BooleanField(
        verbose_name="口不渴", blank=True, null=True)
    thirsty = models.BooleanField(
        verbose_name="渴", blank=True, null=True)
    thirsty_but_not_wanting_to_drink = models.BooleanField(
        verbose_name="渴不欲饮", blank=True, null=True)
    drink_hot_water = models.BooleanField(
        verbose_name="想喝热水", blank=True, null=True)
    not_quenched_by_drinking = models.BooleanField(
        verbose_name="千杯不解渴", blank=True, null=True)

    # 其他相关信息
    additional_notes = models.TextField(
        verbose_name="其他症状描述", blank=True, null=True)
    change_notes = models.TextField(
        verbose_name="本次信息的修改说明", blank=True, null=True)


class NumbnessSymptoms(models.Model):
    belong = models.CharField(verbose_name="是谁的", max_length=20)
    # 麻木症状
    finger_stiff = models.BooleanField(verbose_name="手指僵", blank=True, null=True)
    finger_numb = models.BooleanField(verbose_name="手指麻", blank=True, null=True)
    upper_arm_numb = models.BooleanField(verbose_name="胳膊无力", blank=True, null=True)
    upper_arm_stiff = models.BooleanField(verbose_name="胳膊麻木", blank=True, null=True)
    toe_stiff = models.BooleanField(verbose_name="脚趾僵", blank=True, null=True)
    toe_numb = models.BooleanField(verbose_name="脚趾麻", blank=True, null=True)
    Aching_waist_aching_legs = models.BooleanField(verbose_name="腰酸腿痛", blank=True, null=True)
    General_fatigue = models.BooleanField(verbose_name="全身乏力", blank=True, null=True)
    lower_leg_weak = models.BooleanField(verbose_name="腿没劲", blank=True, null=True)
    lower_leg_numb = models.BooleanField(verbose_name="腿麻木", blank=True, null=True)
    calf_sore = models.BooleanField(verbose_name="小腿酸痛", blank=True, null=True)
    wrist_numb = models.BooleanField(verbose_name="手腕麻", blank=True, null=True)
    wrist_stiff = models.BooleanField(verbose_name="手腕每", blank=True, null=True)
    ankle_numb = models.BooleanField(verbose_name="足腕麻", blank=True, null=True)
    ankle_stiff = models.BooleanField(verbose_name="足腕僵", blank=True, null=True)
    # 其他相关信息
    additional_notes = models.TextField(
        verbose_name="其他症状描述", blank=True, null=True)
    change_notes = models.TextField(
        verbose_name="本次信息的修改说明", blank=True, null=True)


class GynecologicalSymptoms(models.Model):
    belong = models.CharField(verbose_name="是谁的", max_length=20)
    # 女科症状
    dysmenorrhea = models.BooleanField(verbose_name="痛经", blank=True, null=True)
    blood_clots_in_menses = models.BooleanField(verbose_name="经有血块", blank=True, null=True)
    menstruation_advance = models.BooleanField(verbose_name="月经提前", blank=True, null=True)
    menstruation_delay = models.BooleanField(verbose_name="月经延后", blank=True, null=True)
    leukorrhea = models.BooleanField(verbose_name="白带", blank=True, null=True)
    yellow_leukorrhea = models.BooleanField(verbose_name="黄带", blank=True, null=True)
    red_leukorrhea = models.BooleanField(verbose_name="赤带", blank=True, null=True)
    foul_smell = models.BooleanField(verbose_name="气味腥臭", blank=True, null=True)
    vulvar_pruritus = models.BooleanField(verbose_name="外阴瘙痒", blank=True, null=True)

    # 其他女科症状描述
    additional_notes = models.TextField(
        verbose_name="其他症状描述", blank=True, null=True)
    change_notes = models.TextField(
        verbose_name="本次信息的修改说明", blank=True, null=True)


class UrologicalSymptoms(models.Model):
    belong = models.CharField(verbose_name="是谁的", max_length=20)
    # 男科症状
    impotence = models.BooleanField(verbose_name="阳痿", blank=True, null=True)
    premature_ejaculation = models.BooleanField(verbose_name="早泄", blank=True, null=True)
    nocturnal_emission = models.BooleanField(verbose_name="遗精", blank=True, null=True)
    spermatorrhea = models.BooleanField(verbose_name="滑精", blank=True, null=True)
    weak_erection = models.BooleanField(verbose_name="举而不坚", blank=True, null=True)
    decreased_libido = models.BooleanField(verbose_name="性欲减退", blank=True, null=True)
    damp_scrotum = models.BooleanField(verbose_name="阴囊潮湿", blank=True, null=True)
    scrotal_pain = models.BooleanField(verbose_name="阴囊疼痛", blank=True, null=True)
    scrotal_wetness_and_itching = models.BooleanField(verbose_name="阴囊湿痒", blank=True, null=True)

    # 其他男科症状描述
    additional_notes = models.TextField(
        verbose_name="其他症状描述", blank=True, null=True)
    change_notes = models.TextField(
        verbose_name="本次信息的修改说明", blank=True, null=True)


class TongueAppearance(models.Model):
    belong = models.CharField(verbose_name="是谁的", max_length=20)
    Coated_tongue_white = models.BooleanField(verbose_name="舌苔白", blank=True, null=True)
    Coated_tongue_yellow = models.BooleanField(verbose_name="舌苔黄", blank=True, null=True)
    Coated_tongue_thick = models.BooleanField(verbose_name="舌苔厚", blank=True, null=True)
    Coated_tongue_greasy = models.BooleanField(verbose_name="舌苔腻", blank=True, null=True)
    Coated_tongue_slide = models.BooleanField(verbose_name="舌苔滑", blank=True, null=True)
    Body_of_tongue_big = models.BooleanField(verbose_name="舌体大", blank=True, null=True)
    Body_of_tongue_small = models.BooleanField(verbose_name="舌体小", blank=True, null=True)
    Body_of_tongue_crack = models.BooleanField(verbose_name="舌体有裂纹", blank=True, null=True)
    tongue_color_choices = (
        (1, "红"),
        (2, "淡"),
        (3, "白"),
        (4, "灰"),
        (5, "紫"),
        (6, "黑"),
    )
    Tongue_color = models.SmallIntegerField(verbose_name="舌色", choices=tongue_color_choices, blank=True, null=True)
    tongue_quality_choices = (
        (1, "干"),
        (2, "湿")
    )
    tongue_quality = models.SmallIntegerField(verbose_name="舌质", choices=tongue_quality_choices, blank=True,
                                              null=True)
    additional_notes = models.TextField(
        verbose_name="其他症状描述", blank=True, null=True)
    change_notes = models.TextField(
        verbose_name="本次信息的修改说明", blank=True, null=True)


class BowelAndUrinarySymptoms(models.Model):
    belong = models.CharField(verbose_name="是谁的", max_length=20)
    # 大便症状
    regular_bowel_movements = models.BooleanField(
        verbose_name="大便全过程成形", null=True, blank=True)
    hard_start_soft_end = models.BooleanField(
        verbose_name="开头硬结尾稀", null=True, blank=True)
    constipation = models.BooleanField(
        verbose_name="大便干结", null=True, blank=True)
    difficult_to_pass = models.BooleanField(
        verbose_name="大便难下", null=True, blank=True)
    loose_stools = models.BooleanField(
        verbose_name="大便糖稀", null=True, blank=True)
    watery_diarrhea = models.BooleanField(
        verbose_name="大便水泻", null=True, blank=True)
    bowel_movement_frequency = models.PositiveSmallIntegerField(
        verbose_name="大便几天一次", choices=[(1, "一天一次"), (2, "两天一次"), (3, "三天一次")], blank=True, null=True)

    # 小便症状
    frequent_urination = models.BooleanField(
        verbose_name="尿频", null=True, blank=True)
    urination_urgency = models.BooleanField(
        verbose_name="尿急", null=True, blank=True)
    cloudy_urine = models.BooleanField(
        verbose_name="尿浊", null=True, blank=True)
    red_urine = models.BooleanField(
        verbose_name="尿赤", null=True, blank=True)
    hematuria = models.BooleanField(
        verbose_name="血尿", null=True, blank=True)
    urination_pain = models.BooleanField(
        verbose_name="尿痛", null=True, blank=True)
    cloudy_white = models.BooleanField(
        verbose_name="尿白", null=True, blank=True)
    incontinence = models.BooleanField(
        verbose_name="漏尿", null=True, blank=True)
    incomplete_emptying = models.BooleanField(
        verbose_name="尿不尽", null=True, blank=True)
    nocturia = models.PositiveSmallIntegerField(
        verbose_name="夜尿次数", blank=True, null=True)
    history_of_enuresis = models.BooleanField(
        verbose_name="有尿床史", null=True, blank=True)

    additional_notes = models.TextField(
        verbose_name="其他症状描述", blank=True, null=True)
    change_notes = models.TextField(
        verbose_name="本次信息的修改说明", blank=True, null=True)


class WesternMedicineDiagnosis(models.Model):
    belong = models.CharField(verbose_name="是谁的", max_length=20)
    blood_pressure = models.CharField(verbose_name='高血压', blank=True, null=True, max_length=50)
    hyperglycemia = models.CharField(verbose_name='高血糖', blank=True, null=True, max_length=50)
    hyperlipidemia = models.CharField(verbose_name='高血脂', blank=True, null=True, max_length=50)
    hyperuricemia = models.CharField(verbose_name='高尿酸', blank=True, null=True, max_length=50)
    creatinine = models.CharField(verbose_name='肌酐尿素值', blank=True, null=True, max_length=50)
    additional_notes = models.TextField(
        verbose_name="其他症状描述", blank=True, null=True)
    change_notes = models.TextField(
        verbose_name="本次信息的修改说明", blank=True, null=True)


class CurrentMedicalHistory(models.Model):
    belong = models.CharField(verbose_name="是谁的", max_length=20)
    # 症状描述
    symptoms = models.TextField(verbose_name="既往病史", blank=True, null=True)
    change_notes = models.TextField(
        verbose_name="本次信息的修改说明", blank=True, null=True)


class Result(models.Model):
    belong = models.CharField(verbose_name="是谁的", max_length=20)
    symptom = models.TextField(verbose_name="症状", blank=True, null=True)
    prescription = models.TextField(verbose_name="处方", blank=True, null=True)
    additional_notes = models.TextField(
        verbose_name="其他补充", blank=True, null=True)
    change_notes = models.TextField(
        verbose_name="本次信息的修改说明", blank=True, null=True)


class Pulse(models.Model):
    belong = models.CharField(verbose_name="是谁的", max_length=20)
    anion_pulse_late = models.BooleanField(
        verbose_name="阴脉迟", null=True, blank=True)
    anion_pulse_se = models.BooleanField(
        verbose_name="阴脉涩", null=True, blank=True)
    anion_pulse_wei = models.BooleanField(
        verbose_name="阴脉微", null=True, blank=True)
    anion_pulse_huan = models.BooleanField(
        verbose_name="阴脉缓", null=True, blank=True)
    anion_pulse_lao = models.BooleanField(
        verbose_name="阴脉牢", null=True, blank=True)
    anion_pulse_ruo = models.BooleanField(
        verbose_name="阴脉弱", null=True, blank=True)
    anion_pulse_san = models.BooleanField(
        verbose_name="阴脉散", null=True, blank=True)
    anion_pulse_jie = models.BooleanField(
        verbose_name="阴脉结", null=True, blank=True)
    anion_pulse_dai = models.BooleanField(
        verbose_name="阴脉代", null=True, blank=True)
    cation_pulse_shu = models.BooleanField(
        verbose_name="阳脉数", null=True, blank=True)
    cation_pulse_hua = models.BooleanField(
        verbose_name="阳脉滑", null=True, blank=True)
    cation_pulse_hong = models.BooleanField(
        verbose_name="阳脉洪", null=True, blank=True)
    cation_pulse_jin = models.BooleanField(
        verbose_name="阳脉紧", null=True, blank=True)
    cation_pulse_xian = models.BooleanField(
        verbose_name="阳脉弦", null=True, blank=True)
    cation_pulse_ru = models.BooleanField(
        verbose_name="阳脉濡", null=True, blank=True)
    cation_pulse_xi = models.BooleanField(
        verbose_name="阳脉细", null=True, blank=True)
    cation_pulse_cu = models.BooleanField(
        verbose_name="阳脉促", null=True, blank=True)
    cation_pulse_da = models.BooleanField(
        verbose_name="阳脉大", null=True, blank=True)
    additional_notes = models.TextField(
        verbose_name="其他补充", blank=True, null=True)
    change_notes = models.TextField(
        verbose_name="处方修改说明", blank=True, null=True)
