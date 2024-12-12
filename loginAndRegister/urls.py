from django.urls import path

from loginAndRegister.views import Login, Register, RegisterForDoctor, LoginForDoctor, LoginForAdmin, _RegisterForCheck, \
    _RegisterForCrawl, get_json_info, logout

urlpatterns = [
    path("", Login.as_view()),
    path("login/", Login.as_view(), name="login"),
    path("register/", Register.as_view(), name="register"),
    path("register/doctor/", RegisterForDoctor.as_view(), name="registerForDoctor"),
    path("login/doctor/", LoginForDoctor.as_view(), name="loginForDoctor"),
    path("login/admin/", LoginForAdmin.as_view(), name="loginForAdmin"),
    path("register/check/", _RegisterForCheck.as_view(), name="registerForCheck"),
    path("register/crawl/", _RegisterForCrawl.as_view(), name="registerForCrawl"),
    path("info/", get_json_info),
    path("logout/", logout)
]
