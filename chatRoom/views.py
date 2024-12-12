from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, redirect
import os
from django.conf import settings
import hashlib
from loginAndRegister.models import userInfo
from personal_info_new.disease_form_new import TotalForNoFirst
from django.apps import apps
from django.db import models


def user_assignment_doctor(req):
    user_id = req.session.get('id')
    user_data = userInfo.objects.filter(id=user_id).first()
    data = {
        "username": user_data.username,
        "id": user_id,
        "first": user_data.first
    }
    return render(req, 'chatRoom/assignment/for_user.html', data)


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']

        md5 = hashlib.md5()
        fileInfo = file.name.split('.')
        md5.update(fileInfo[0].encode('utf-8'))
        new_file_name = f'{md5.hexdigest()}.{fileInfo[-1]}'

        file_path = os.path.join(settings.BASE_DIR, 'staticfiles/tmp/upload/', new_file_name)
        with open(file_path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        file_url = settings.STATIC_URL + 'tmp/upload/' + new_file_name
        return JsonResponse({'file_url': file_url})
    return JsonResponse({'error': 'Invalid request'}, status=400)


def in_chat_room(req, room_number):
    return render(req, 'chatRoom/room/chat_with_doctor.html', {"room_number": room_number})


def doctor_message_list(req):
    if req.session.get('role', None) != "doctor":
        req.session.clear()
        return redirect("/")
    return render(req, 'chatRoom/assignment/doctorMessageList.html')


def room_for_doctor(req, room_number):
    patient_id = req.GET.get('patient_id', -1)
    patient_name = req.GET.get('patient_name', -1)
    user = userInfo.objects.filter(id=patient_id).first()
    first = user.first

    return render(req, 'chatRoom/room/for_doctor.html',
                  {"room": room_number, "patient_id": patient_id, "patient_name": patient_name, "first": first})


@csrf_exempt
def doctor_room_side(req):
    patient_id = req.POST.get('patient_id', -1)
    user = userInfo.objects.filter(id=patient_id).first()
    first = user.first
    phone = user.phoneNumber
    if first:
        data = [
            '个人信息',
            "您感觉怕风怕冷的情况？",
            '您身体的某个部位经常感觉发热的情况？',
            '您身体的某个部位经常冰凉的情况？',
            "您平时的出汗情况？",
            '大便及排气情况？',
            '小便情况？',
            '您的饮水情况？',
            '您的饮食情况？',
            '您咳嗽吐痰的情况？',
            '您的情绪情况？',
            '五官？',
            '睡眠情况？',
            "有无疼痛感觉（痛的部位）？",
            '口中感受？',
            '体力情况？',
            '出血情况？',
            '习惯？',
            '大便一天几次？',
            "一夜排尿几次？",
            "夜间几点钟睡？",
            "夜间醒在几点钟？",
            '既往病史',
            '诊断结果',
            '选择跟踪项目'
        ]
    else:
        data = [
            '个人信息',
            '选择跟踪项目'
        ]
        total = TotalForNoFirst(phone=phone)
        other_data = list(total.data.keys())
        data = data + other_data

    return render(req, 'chatRoom/room/doctor_room_side.html',
                  {'data': data})


@csrf_exempt
def create_new(req):
    if req.method == 'POST':
        patient_id = req.POST.get('patient_id', -1)
        user = userInfo.objects.filter(id=patient_id).first()
        phone = user.phoneNumber
        total = TotalForNoFirst(phone=phone)
        total.create_tables()
        return HttpResponse(status=200)
    return HttpResponse(status=500)


@csrf_exempt
def renew_table(req):
    if req.method == 'POST':
        patient_id = req.POST.get('patient_id', -1)
        users = userInfo.objects.filter(id=patient_id)
        users.update(first=True)
        user = users.first()
        phone = user.phoneNumber
        total = TotalForNoFirst(phone=phone)
        total.delete()
        return HttpResponse(status=200)
    return HttpResponse(status=500)


@csrf_exempt
def get_choose(req):
    if req.method == 'POST':
        patient_id = req.POST.get('patient_id', -1)
        user = userInfo.objects.filter(id=patient_id).first()
        phone = user.phoneNumber
        result = get_true_fields_verbose(phone)
        return render(req, 'chatRoom/room/choose_table.html', {'data': result})
    return HttpResponse(status=500)


def get_true_fields_verbose(belong_value):
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

    result = {}

    for model_name in all_fields.keys():
        model = apps.get_model('personal_info_new', model_name)
        record = model.objects.filter(belong=belong_value).first()
        true_fields = []
        for field in model._meta.get_fields():
            # 只检查BooleanField类型字段
            if isinstance(field, models.BooleanField) and getattr(record, field.name) == True:
                true_fields.append(field.verbose_name)
            if isinstance(field, models.CharField):
                if field.verbose_name != "是谁的":
                    text_value = getattr(record, field.name, "")
                    if text_value:
                        true_fields.append(text_value)

        if true_fields:
            result[all_fields[model_name]] = true_fields

    return result
