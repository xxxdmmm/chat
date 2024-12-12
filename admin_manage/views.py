from django.shortcuts import render, HttpResponse, redirect
from menu_and_select.models import doctorInfos
from django.views.decorators.csrf import csrf_exempt
from pharmacy.models import UserPharmacy


# Create your views here.

def for_admin(req):
    if req.session.get('role', None) != "admin":
        req.session.clear()
        return redirect("/")
    doctors = doctorInfos.objects.all()
    doctorData = {}
    for doctor in doctors:
        doctorData[doctor.id] = doctor.doctor_name
    data = {
        "doctors": doctorData
    }
    return render(req, 'admin_manage/admin.html', data)


@csrf_exempt
def assign_doctor(req):
    return HttpResponse("分配成功！", status=500)


def get_all_pharmacy(req):
    if req.session.get('role', None) != "admin":
        req.session.clear()
        return redirect("/")
    data = {
        'data': UserPharmacy.objects.all()
    }
    return render(req, 'admin_manage/pharmacy_info.html', data)
