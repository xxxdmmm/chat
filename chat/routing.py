from django.urls import re_path, path
from chatRoom import consumers

websocket_urlpatterns = [
    re_path(r'room/number/(?P<group>[^/]+)/$', consumers.ChatConsumer.as_asgi()),
    re_path(r'doctor/message-list/(?P<doctorID>\w+)/$', consumers.DoctorMessageList.as_asgi()),
    re_path(r'user/message-list/(?P<userID>\w+)/$', consumers.UserMessageList.as_asgi()),
    path('mange-list/', consumers.AdminMessageList.as_asgi()),
    path('pharmacy/', consumers.Pharmacy.as_asgi())
]
