from django.shortcuts import render
from pharmacy.models import CheckPeople, CrawlPeople
from personal_info.models import Result
from personal_info_new.models import WindAndCold
from personal_info_new.disease_form_new import Total
from django import forms
from loginAndRegister.models import userInfo
from personal_info_new.models import Choose, TABLE

total = Total()


# Create your views here.

class Test(forms.ModelForm):
    class Meta:
        model = WindAndCold
        exclude = ["belong"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})


def test(req):
    # userInfo.objects.filter().delete()
    # total.delete(phone="15703052124")
    # patient_id = req.POST.get('patient_id', -1)
    # user = userInfo.objects.filter(id=patient_id).first()
    pass
