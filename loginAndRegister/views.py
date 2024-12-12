from abc import ABCMeta, abstractmethod

from django.forms import ModelForm
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from loginAndRegister.some_forms import *
from personal_info_new.disease_form_new import Total as Total_new
from django.views import View
from django.conf import settings

# Create your views here.
disease_info_new = Total_new()


@csrf_exempt
def get_json_info(request):
    return HttpResponse(json.dumps(dict(request.session)), content_type="application/json")


@require_http_methods(['GET'])
def logout(req):
    req.session.clear()
    return redirect('/')


def identify(req, form, data):
    _form = form(data=data)
    if _form.is_valid():
        req.session['id'] = _form.cleaned_data['id']
        req.session['username'] = _form.cleaned_data['username']
        req.session['phone'] = _form.cleaned_data['phoneNumber']
        req.session['first'] = _form.cleaned_data.get('first', False)
        req.session['login'] = 0
        req.session['port'] = settings.MAIN_PORT
    return _form, _form.is_valid()


class Login(View):
    def get(self, request):
        forms = LoginForm()
        return render(request, 'loginAndRegister/login.html', {'forms': forms})

    def post(self, request):
        forms, valid = identify(request, LoginForm, request.POST)
        if valid:
            request.session['login'] = 1
            request.session['role'] = "patient"
            return redirect(f'/user/personal/')
        else:
            return render(request, 'loginAndRegister/login.html', {'forms': forms})


class LoginForDoctor(View):
    def get(self, request):
        forms = DoctorLoginForm()
        return render(request, 'loginAndRegister/login_for_doctor.html', {'forms': forms})

    def post(self, request):
        forms, valid = identify(request, DoctorLoginForm, request.POST)
        if valid:
            request.session['login'] = 1
            request.session['role'] = "doctor"
            return redirect('/doctor/message/')
        else:
            return render(request, 'loginAndRegister/login_for_doctor.html', {'forms': forms})


class LoginForAdmin(View):
    def get(self, request):
        forms = AdminLoginForm()
        return render(request, 'loginAndRegister/login_for_admin.html', {'forms': forms})

    def post(self, request):
        forms, valid = identify(request, AdminLoginForm, request.POST)
        if valid:
            request.session['login'] = 1
            request.session['role'] = "admin"
            return redirect('/for-admin/')
        else:
            return render(request, 'loginAndRegister/login_for_admin.html', {'forms': forms})


class Register(View):
    def get(self, request):
        forms = RegisterForm()
        return render(request, 'loginAndRegister/register.html', {"forms": forms})

    def post(self, request):
        forms = RegisterForm(data=request.POST)
        if forms.is_valid():
            forms.save()
            disease_info_new.create(request.POST['phoneNumber'])
            return render(request, 'loginAndRegister/register.html', {'forms': forms, 'warn': "注册成功!"})
        else:
            return render(request, 'loginAndRegister/register.html', {'forms': forms})


class RegisterForDoctor(View):
    def get(self, request):
        forms = DoctorRegisterForm()
        return render(request, 'loginAndRegister/register_for_doctor.html', {'forms': forms})

    def post(self, request):
        forms = DoctorRegisterForm(data=request.POST)
        if forms.is_valid():
            forms.save()
            return render(request, 'loginAndRegister/register_for_doctor.html', {'forms': forms, 'warn': "注册成功!"})
        else:
            return render(request, 'loginAndRegister/register_for_doctor.html', {'forms': forms})


class _RegisterForCheck(View):
    def get(self, request):
        forms = RegisterForCheck()
        return render(request, 'loginAndRegister/register_for_check.html', {'forms': forms})

    def post(self, request):
        forms = RegisterForCheck(data=request.POST)
        if forms.is_valid():
            forms.save()
            return render(request, 'loginAndRegister/register_for_check.html', {'forms': forms, 'warn': "注册成功!"})
        else:
            return render(request, 'loginAndRegister/register_for_check.html', {'forms': forms})


class _RegisterForCrawl(View):
    def get(self, request):
        forms = RegisterForCrawl()
        return render(request, 'loginAndRegister/register_for_crawl.html', {'forms': forms})

    def post(self, request):
        forms = RegisterForCrawl(data=request.POST)
        if forms.is_valid():
            forms.save()
            return render(request, 'loginAndRegister/register_for_crawl.html', {'forms': forms, 'warn': "注册成功!"})
        else:
            return render(request, 'loginAndRegister/register_for_crawl.html', {'forms': forms})
