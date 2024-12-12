from django.shortcuts import render, HttpResponse
from personal_info_new.models import Result
from loginAndRegister.models import userInfo
import json
from django.views.decorators.csrf import csrf_exempt
from django import forms
from pharmacy.models import UserPharmacy
from django.conf import settings
import os


# Create your views here.

def pharmacy(re):
    return render(re, 'pharmacy/pharmacy.html')


class CheckAndCrawl(forms.ModelForm):
    class Meta:
        managed = True
        model = UserPharmacy
        fields = ['crawl_name', 'check_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control",
                "placeholder": field.label
            }


@csrf_exempt
def get_form_check_and_crawl(req):
    if req.method == 'POST':
        form = CheckAndCrawl()
        crawl_name_field = form['crawl_name'].as_widget()
        check_name_field = form['check_name'].as_widget()
        data = {
            'status': 200,
            'crawl_name_field': crawl_name_field,
            'check_name_field': check_name_field
        }
        return HttpResponse(json.dumps(data), status=200)
    data = {
        'status': 500
    }
    return HttpResponse(json.dumps(data), status=500)


@csrf_exempt
def get_result(re):
    patient_id = re.POST.get('patient_id', None)
    if patient_id is None:
        data = {
            'status': 500
        }
        return HttpResponse(json.dumps(data), status=500)
    phone = userInfo.objects.filter(id=patient_id).first().phoneNumber
    result = Result.objects.filter(belong=phone).first()
    data = {
        'status': 200,
        'symptom': result.symptom,
        'prescription': result.prescription,
        'patient_id': patient_id
    }
    return HttpResponse(json.dumps(data), status=200)


@csrf_exempt
def upload_data(req):
    if req.method == 'POST':
        prescription = req.POST.get('prescription')
        symptom = req.POST.get('symptom')
        doctor_name = req.POST.get('doctor_name')
        patient_name = req.POST.get('patient_name')
        crawl_name = int(req.POST.get('crawl_name'))
        check_name = int(req.POST.get('check_name'))
        patient_id = req.POST.get('patient_id')
        img = req.FILES.get('image')
        
        img_path = os.path.join(settings.BASE_DIR, 'staticfiles/pharmacy_image', f'{patient_id}.jpg')
        relative_path = os.path.join('static/pharmacy_image', f'{patient_id}.jpg')    

        with open(img_path, 'wb') as f:
            for chunk in img.chunks():
                f.write(chunk)

        target = UserPharmacy.objects.filter(belong=patient_id)
        if target.exists():
            target.update(doctor_name=doctor_name, crawl_name_id=crawl_name, check_name_id=check_name,
                          photo_path=relative_path, prescription=prescription, symptom=symptom)
        else:
            UserPharmacy.objects.create(doctor_name=doctor_name, user_name=patient_name, check_name_id=check_name,
                                        crawl_name_id=crawl_name, photo_path=relative_path, prescription=prescription,
                                        symptom=symptom, belong=patient_id)

        return HttpResponse(json.dumps({
            "status": 200
        }), status=200)
    return HttpResponse(json.dumps({
        "status": 500
    }), status=500)
