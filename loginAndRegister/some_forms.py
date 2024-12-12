from django import forms
from loginAndRegister.models import userInfo, Admin
from menu_and_select.models import doctorInfos
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from pharmacy.models import CheckPeople, CrawlPeople


class RegisterForCheck(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=9, label="密码")
    name = forms.CharField(widget=forms.TextInput, min_length=2, label="账户名")
    phoneNumber = forms.CharField(label="手机号", validators=[RegexValidator(r'^1[3-9]\d{9}$', "手机号格式错误")])

    class Meta:
        managed = True
        model = CheckPeople
        fields = ["name", "password", "phoneNumber"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control",
                "placeholder": field.label
            }

    def clean_phoneNumber(self):
        phoneNumber = self.cleaned_data['phoneNumber']
        target = CheckPeople.objects.filter(phoneNumber=phoneNumber)
        if target.exists():
            raise ValidationError("手机号已注册!")
        return phoneNumber


class RegisterForCrawl(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=9, label="密码")
    name = forms.CharField(widget=forms.TextInput, min_length=2, label="账户名")
    phoneNumber = forms.CharField(label="手机号", validators=[RegexValidator(r'^1[3-9]\d{9}$', "手机号格式错误")])

    class Meta:
        managed = True
        model = CrawlPeople
        fields = ["name", "password", "phoneNumber"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control",
                "placeholder": field.label
            }

    def clean_phoneNumber(self):
        phoneNumber = self.cleaned_data['phoneNumber']
        target = CrawlPeople.objects.filter(phoneNumber=phoneNumber)
        if target.exists():
            raise ValidationError("手机号已注册!")
        return phoneNumber


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=9, label="密码")
    username = forms.CharField(widget=forms.TextInput, min_length=2, label="账户名")
    phoneNumber = forms.CharField(label="手机号", validators=[RegexValidator(r'^1[3-9]\d{9}$', "手机号格式错误")])

    class Meta:
        managed = True
        model = userInfo
        fields = ["username", "password", "phoneNumber"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control",
                "placeholder": field.label
            }

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        phoneNumber = cleaned_data.get('phoneNumber')

        users = userInfo.objects.filter(username=username, password=password, phoneNumber=phoneNumber)
        if users.exists():
            user = users.first()
            cleaned_data['id'] = user.id
            cleaned_data['phoneNumber'] = phoneNumber
            cleaned_data['first'] = user.first
            return cleaned_data
        raise ValidationError("信息错误!")


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=9, label="密码")
    username = forms.CharField(widget=forms.TextInput, min_length=2, label="账户名")
    phoneNumber = forms.CharField(label="手机号", validators=[RegexValidator(r'^1[3-9]\d{9}$', "手机号格式错误")])

    class Meta:
        managed = True
        model = userInfo
        fields = ["username", "password", "phoneNumber", "age", "sex"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control",
                "placeholder": field.label
            }

    def clean_phoneNumber(self):
        phoneNumber = self.cleaned_data['phoneNumber']
        user = userInfo.objects.filter(phoneNumber=phoneNumber)
        if user.exists():
            raise ValidationError("手机号已注册!")
        return phoneNumber


class DoctorRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=9, label="密码")
    doctor_name = forms.CharField(widget=forms.TextInput, min_length=2, label="账户名")
    phoneNumber = forms.CharField(label="手机号", validators=[RegexValidator(r'^1[3-9]\d{9}$', "手机号格式错误")])

    class Meta:
        managed = True
        model = doctorInfos
        fields = ["doctor_name", "password", "phoneNumber", "department", "hospital", "age", "sex"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control",
                "placeholder": field.label
            }

    def clean_phoneNumber(self):
        # print(self.cleaned_data)
        phoneNumber = self.cleaned_data['phoneNumber']
        doctor = doctorInfos.objects.filter(phoneNumber=phoneNumber)
        if doctor.exists():
            raise ValidationError("手机号已注册!")
        return phoneNumber


class DoctorLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=9, label="密码")
    doctor_name = forms.CharField(widget=forms.TextInput, min_length=2, label="账户名")
    phoneNumber = forms.CharField(label="手机号", validators=[RegexValidator(r'^1[3-9]\d{9}$', "手机号格式错误")])

    class Meta:
        managed = True
        model = doctorInfos
        fields = ["doctor_name", "password", "phoneNumber"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control",
                "placeholder": field.label
            }

    def clean(self):
        cleaned_data = super().clean()
        doctor_name = cleaned_data.get("doctor_name")
        password = cleaned_data.get("password")
        phoneNumber = cleaned_data.get('phoneNumber')
        doctors = doctorInfos.objects.filter(doctor_name=doctor_name, password=password, phoneNumber=phoneNumber)
        if doctors.exists():
            doctor = doctors.first()
            cleaned_data["username"] = doctor_name
            cleaned_data['id'] = doctor.id
            return cleaned_data
        raise ValidationError("信息错误!!")


class AdminLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=9, label="密码")
    username = forms.CharField(widget=forms.TextInput, min_length=2, label="账户名")
    phoneNumber = forms.CharField(label="手机号", validators=[RegexValidator(r'^1[3-9]\d{9}$', "手机号格式错误")])

    class Meta:
        managed = True
        model = Admin
        fields = ["username", "password", "phoneNumber"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {
                "class": "form-control",
                "placeholder": field.label
            }

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        phoneNumber = cleaned_data.get('phoneNumber')
        admin = Admin.objects.filter(username=username, password=password, phoneNumber=phoneNumber)
        if admin.exists():
            admin = admin.first()
            cleaned_data['id'] = admin.id
            return cleaned_data
        raise ValidationError("信息错误!!")
