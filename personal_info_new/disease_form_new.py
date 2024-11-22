from django.forms import ModelForm
from personal_info_new.models import *
from django import forms
from loginAndRegister.models import userInfo
from personal_info_new.models import Choose


class WindAndColdForm(ModelForm):
    class Meta:
        managed = True
        model = WindAndCold
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget = forms.CheckboxInput()


class HeatSymptomsForm(ModelForm):
    class Meta:
        managed = True
        model = HeatSymptoms
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget = forms.CheckboxInput()


class ColdSymptomsForm(ModelForm):
    class Meta:
        managed = True
        model = ColdSymptoms
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget = forms.CheckboxInput()


class SweatingSymptomsForm(ModelForm):
    class Meta:
        managed = True
        model = SweatingSymptoms
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget = forms.CheckboxInput()


class BowelAndFlatulenceSymptomsForm(ModelForm):
    class Meta:
        managed = True
        model = BowelAndFlatulenceSymptoms
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget = forms.CheckboxInput()


class UrinationSymptomsForm(ModelForm):
    class Meta:
        managed = True
        model = UrinationSymptoms
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget = forms.CheckboxInput()


class HydrationSymptomsForm(ModelForm):
    class Meta:
        managed = True
        model = HydrationSymptoms
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget = forms.CheckboxInput()


class DietSymptomsForm(ModelForm):
    class Meta:
        managed = True
        model = DietSymptoms
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget = forms.CheckboxInput()


class CoughSymptomsForm(ModelForm):
    class Meta:
        managed = True
        model = CoughSymptoms
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget = forms.CheckboxInput()


class EmotionalSymptomsForm(ModelForm):
    class Meta:
        managed = True
        model = EmotionalSymptoms
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget = forms.CheckboxInput()


class FacialSymptomsForm(ModelForm):
    class Meta:
        managed = True
        model = FacialSymptoms
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget = forms.CheckboxInput()


class SleepSymptomsForm(ModelForm):
    class Meta:
        managed = True
        model = SleepSymptoms
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget = forms.CheckboxInput()


class PainSymptomsForm(ModelForm):
    class Meta:
        managed = True
        model = PainSymptoms
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget = forms.CheckboxInput()


class OralSymptomsForm(ModelForm):
    class Meta:
        managed = True
        model = OralSymptoms
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget = forms.CheckboxInput()


class PhysicalSymptomsForm(ModelForm):
    class Meta:
        managed = True
        model = PhysicalSymptoms
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget = forms.CheckboxInput()


class BleedingSymptomsForm(ModelForm):
    class Meta:
        managed = True
        model = BleedingSymptoms
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget = forms.CheckboxInput()


class HabitSymptomsForm(ModelForm):
    class Meta:
        managed = True
        model = HabitSymptoms
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget = forms.CheckboxInput()


class HowMangBigForm(ModelForm):
    class Meta:
        managed = True
        model = HowMangBig
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control",
                "placeholder": field.label
            }


class HowNightSleepForm(ModelForm):
    class Meta:
        managed = True
        model = HowNightSleep
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control",
                "placeholder": field.label
            }


class HowNightAwakeForm(ModelForm):
    class Meta:
        managed = True
        model = HowNightAwake
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control",
                "placeholder": field.label
            }


class HowMangSmallForm(ModelForm):
    class Meta:
        managed = True
        model = HowMangSmall
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control",
                "placeholder": field.label
            }


class CurrentMedicalHistoryForm(ModelForm):
    class Meta:
        managed = True
        model = CurrentMedicalHistory
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control",
                "placeholder": field.label
            }


class ResultForm(ModelForm):
    class Meta:
        managed = True
        model = Result
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control",
                "placeholder": field.label
            }


class ChooseForm(ModelForm):
    class Meta:
        managed = True
        model = Choose
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget = forms.CheckboxInput()


class Total:
    data = {
        "您感觉怕风怕冷的情况？": WindAndColdForm,
        '您身体的某个部位经常感觉发热的情况？': HeatSymptomsForm,
        '您身体的某个部位经常冰凉的情况？': ColdSymptomsForm,
        "您平时的出汗情况？": SweatingSymptomsForm,
        '大便及排气情况？': BowelAndFlatulenceSymptomsForm,
        '小便情况？': UrinationSymptomsForm,
        '您的饮水情况？': HydrationSymptomsForm,
        '您的饮食情况？': DietSymptomsForm,
        '您咳嗽吐痰的情况？': CoughSymptomsForm,
        '您的情绪情况？': EmotionalSymptomsForm,
        '五官？': FacialSymptomsForm,
        '睡眠情况？': SleepSymptomsForm,
        "有无疼痛感觉（痛的部位）？": PainSymptomsForm,
        '口中感受？': OralSymptomsForm,
        '体力情况？': PhysicalSymptomsForm,
        '出血情况？': BleedingSymptomsForm,
        '习惯？': HabitSymptomsForm,
        '大便一天几次？': HowMangBigForm,
        "一夜排尿几次？": HowMangSmallForm,
        "夜间几点钟睡？": HowNightSleepForm,
        "夜间醒在几点钟？": HowNightAwakeForm,
        '既往病史': CurrentMedicalHistoryForm,
        '诊断结果': ResultForm,
        '选择跟踪项目': ChooseForm,
    }

    def __init__(self):
        pass

    def create(self, phone):
        for name, FormClass in self.data.items():
            model = FormClass.Meta.model
            model.objects.create(belong=phone)

    def delete(self, phone):
        for name, FormClass in self.data.items():
            model = FormClass.Meta.model
            model.objects.filter(belong=phone).delete()

    def show(self, phone, which=None, form=None):
        data = {}
        for name, FormClass in self.data.items():
            model = FormClass.Meta.model
            person_data = model.objects.filter(belong=phone).first()
            data[name] = FormClass(instance=person_data)
        if which and form:
            data[which] = form
        return data

    def change(self, phone, in_data, which):
        modelform = self.data[which]
        model = modelform.Meta.model
        person_data = model.objects.filter(belong=phone).first()
        form = modelform(data=in_data, instance=person_data)
        if form.is_valid():
            form.save()
        return self.show(phone, which=which, form=form), form.is_valid()


class TotalForNoFirst:
    def __init__(self, phone):
        self.data = {}
        self.phone = phone
        self.change_data_dict()

    def delete(self):
        TABLE.objects.filter(belong=self.phone).delete()

    def create_tables(self):
        TABLE.objects.create(belong=self.phone)

    def __table_choose_get(self, field):
        class Form(ModelForm):
            class Meta:
                managed = True
                model = TABLE
                fields = [field]

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                for name, field in self.fields.items():
                    field.widget.attrs = {
                        "class": "form-control",
                        "placeholder": field.label
                    }

        return Form

    def change_data_dict(self):
        all_fields = {
            "windAndCold": "您感觉怕风怕冷的情况？",
            "heatSymptoms": '您身体的某个部位经常感觉发热的情况？',
            "coldSymptoms": '您身体的某个部位经常冰凉的情况？',
            "sweatingSymptoms": "您平时的出汗情况？",
            "bowelAndFlatulenceSymptoms": '大便及排气情况？',
            "urinationSymptoms": '小便情况？',
            "hydrationSymptoms": '您的饮水情况？',
            "dietSymptoms": '您的饮食情况？',
            "coughSymptoms": '您咳嗽吐痰的情况？',
            "emotionalSymptoms": '您的情绪情况？',
            "facialSymptoms": '五官？',
            "sleepSymptoms": '睡眠情况？',
            "painSymptoms": "有无疼痛感觉（痛的部位）？",
            "oralSymptoms": '口中感受？',
            "physicalSymptoms": '体力情况？',
            "bleedingSymptoms": '出血情况？',
            "habitSymptoms": '习惯？',
            "howMangBig": '大便一天几次？',
            "howNightSleep": "夜间几点钟睡？",
            "howNightAwake": "夜间醒在几点钟？",
            "howMangSmall": "一夜排尿几次？",
        }
        chooses = Choose.objects.filter(belong=self.phone).values().first()
        for name, value in chooses.items():
            if name == 'id' or name == 'belong':
                continue
            if value:
                self.data[all_fields[name]] = self.__table_choose_get(name)
        self.data['既往病史'] = CurrentMedicalHistoryForm
        self.data['诊断结果'] = ResultForm
        self.data['处方'] = self.__table_choose_get("medicine")

    def show(self, phone, which=None, form=None):
        assert phone == self.phone, "验证凭证不一致"
        data = {}
        for name, FormClass in self.data.items():
            model = FormClass.Meta.model
            person_data = model.objects.filter(belong=phone).order_by('id').last()
            data[name] = FormClass(instance=person_data)
        if which and form:
            data[which] = form
        return data

    def change(self, phone, in_data, which):
        assert phone == self.phone, "验证凭证不一致"
        modelform = self.data[which]
        model = modelform.Meta.model
        person_data = model.objects.filter(belong=phone).order_by('id').last()
        form = modelform(data=in_data, instance=person_data)
        if form.is_valid():
            form.save()
        return self.show(phone=phone, which=which, form=form), form.is_valid()
