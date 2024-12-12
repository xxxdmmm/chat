from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
from django.conf import settings
from menu_and_select.models import doctorInfos
from django.forms import ModelForm
from django import forms
from loginAndRegister.models import userInfo
from personal_info_new.disease_form_new import Total as Total_new
from personal_info_new.disease_form_new import TotalForNoFirst
import json
from personal_info_new.models import Choose, TABLE

# Create your views here.
#
disease_info_new = Total_new()


class UserModelForm(ModelForm):
    username = forms.CharField(disabled=True, label="名字")
    phoneNumber = forms.CharField(disabled=True, label="电话")

    class Meta:
        managed = True
        model = userInfo
        fields = ["username", "age", "sex", "phoneNumber", "weight", 'high']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control",
                "placeholder": field.label
            }


def user_page(req):
    if req.session.get('role', None) != "patient":
        req.session.clear()
        return redirect("/")
    user_id = req.session.get('id')
    user = userInfo.objects.get(id=user_id)
    first = user.first
    if req.method == 'GET':
        form = UserModelForm(instance=user)
        other_forms = disease_info_new.show(user.phoneNumber)
        if first:
            other_forms.pop('选择跟踪项目')
            datas = {
                'data': {
                    '个人信息': form
                },
                'first': first,
                'patient_id': user_id
            }
            datas['data'].update(other_forms)
            return render(req, 'personal_info/user_page.html', datas)
        else:
            other_forms = {
                '既往病史': other_forms['既往病史'],
                '诊断结果': other_forms['诊断结果']
            }
            datas = {
                'data': {
                    '个人信息': form
                },
                'first': first,
                'patient_id': user_id
            }
            datas['data'].update(other_forms)
            return render(req, 'personal_info/user_page.html', datas)

    which = req.POST.get('which')
    if which == '个人信息':
        form = UserModelForm(data=req.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
    else:
        other_forms, change_success = disease_info_new.change(phone=user.phoneNumber, in_data=req.POST, which=which)
        if change_success:
            return HttpResponse(status=200)
    return HttpResponse(status=500)


####################################################################################################################

def get_patient_form(request, user_id):
    user = userInfo.objects.get(id=user_id)
    if not user.first:
        disease_info_bak = TotalForNoFirst(phone=user.phoneNumber)
    else:
        disease_info_bak = disease_info_new

    if request.method == 'GET':
        field = request.GET.get('field')
        form = UserModelForm(instance=user)
        other_forms = disease_info_bak.show(user.phoneNumber)
        forms = {
            '个人信息': form
        }
        forms.update(other_forms)
        if not user.first:
            info = disease_info_new.data['选择跟踪项目'].Meta.model.objects.filter(
                belong=user.phoneNumber).first()
            forms['选择跟踪项目'] = disease_info_new.data['选择跟踪项目'](
                instance=info)

        context = {
            'forms': forms[field],
            'name': field
        }
        return render(request, 'chatRoom/patient_info.html', context)

    field = request.POST.get('field')
    if field == '个人信息':
        form = UserModelForm(data=request.POST, instance=user)
        data = {
            'field': field
        }
        if form.is_valid():
            form.save()
        return HttpResponse(json.dumps(data))
    else:
        if field == '选择跟踪项目':
            userInfo.objects.filter(phoneNumber=user.phoneNumber).update(first=False)
            other_forms, change_success = disease_info_new.change(phone=user.phoneNumber, in_data=request.POST,
                                                                  which=field)
            data = {
                'field': field
            }
            if change_success:
                return HttpResponse(json.dumps(data))
            return render(request, 'error_page.html')

        other_forms, change_success = disease_info_bak.change(phone=user.phoneNumber, in_data=request.POST, which=field)
        data = {
            'field': field
        }
        if change_success:
            return HttpResponse(json.dumps(data))
    return render(request, 'error_page.html')


class DoctorModelForm(ModelForm):
    phoneNumber = forms.CharField(disabled=True, label="电话")

    class Meta:
        managed = True
        model = doctorInfos
        fields = ["department", "hospital", "introduction", "phoneNumber"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control",
                "placeholder": field.label
            }


@csrf_exempt
def make_better_table(req):
    if req.method == 'POST':
        patient_id = req.POST.get('patient_id', -1)
        user = userInfo.objects.filter(id=patient_id).first()
        phone = user.phoneNumber
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
            'timestamp': "就诊时间",
            'medicine': "处方"
        }

        user_chooses = [choose for choose, value in Choose.objects.filter(belong=phone).values().first().items() if
                        value is True]

        user_chooses.insert(0, "timestamp")
        user_chooses.append('medicine')
        data = TABLE.objects.filter(belong=phone).values(*user_chooses)
        return_data = {}
        for i in data:
            time = i.get("timestamp")
            time = time.strftime('%Y-%m-%d')
            i.pop("timestamp")
            return_data[time] = i

        user_chooses = [all_fields[item] for item in user_chooses]
        return_all_data = {
            'columns': user_chooses,
            'data': return_data
        }
        return render(req, 'personal_info/make_table.html', return_all_data)

    return render(req, 'error_page.html')
