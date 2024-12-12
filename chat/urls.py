"""
URL configuration for chat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from loginAndRegister.views import *
from chatRoom.views import *
from menu_and_select.views import *
from personal_info.views import *
from admin_manage.views import *
from pharmacy.views import *
from django.views import static  ##新增
from django.conf import settings  ##新增

urlpatterns = [
    path("", include("loginAndRegister.urls")),
    re_path(r'^static/(?P<path>.*)$', static.serve,
            {'document_root': settings.STATIC_ROOT}, name='static'),
    path('upload/', upload_file),
    path('user/personal/', user_page),
    path('get/patient/<int:user_id>/info/', get_patient_form),
    path('get/patient/table/', make_better_table),
    path('user/request/', user_assignment_doctor),
    path('doctor/message/', doctor_message_list),
    path('room/forDoctor/<str:room_number>/', room_for_doctor),
    path('room/patient/<str:room_number>/', in_chat_room),
    path('room/sideDoctor/get/', doctor_room_side),
    path('room/table/create/', create_new),
    path('get/patient/choose/', get_choose),
    path('renew/table/', renew_table),
    path('for-admin/', for_admin),
    path('assign-doctor/', assign_doctor),
    path('pharmacy/', pharmacy),
    path('get_result/', get_result),
    path('get_form_check_and_crawl/', get_form_check_and_crawl),
    path('upload_pharmacy_info/', upload_data),
    path('get/all-pharmacy/info/', get_all_pharmacy)
]
