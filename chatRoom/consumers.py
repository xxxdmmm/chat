from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json

room_people_count = {}


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.group_name = None

    async def websocket_connect(self, message):
        await self.accept()
        self.group_name = self.scope['url_route']['kwargs'].get('group')
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        # 初始化组的连接计数
        if self.group_name not in room_people_count:
            room_people_count[self.group_name] = set()
        room_people_count[self.group_name].add(self.channel_name)

    async def websocket_receive(self, message):
        group = self.group_name
        connection_count = len(room_people_count.get(self.group_name, set()))
        # print(connection_count)
        if connection_count <= 1:
            # print("发送给自己")
            await self.send(text_data=json.dumps({'status': 'false'}))
        else:
            await self.channel_layer.group_send(
                group,
                {
                    "type": "chat.message",
                    "message": message,
                    "sender_channel_name": self.channel_name,
                }
            )

    async def chat_message(self, event):
        message = event['message']['text']
        sender_channel_name = event['sender_channel_name']
        if message == "<|come in|>":
            data = {
                'status': 'other-in'
            }
        elif message == "<|come out|>":
            data = {
                'status': 'other-out'
            }
        else:
            data = {
                "message": message,
                'status': 'true'
            }
        if self.channel_name != sender_channel_name:
            await self.send(text_data=json.dumps(data))

    async def websocket_disconnect(self, message):
        group = self.group_name
        await self.channel_layer.group_send(
            group,
            {
                "type": "chat.message",
                "message": {'text': "<|come out|>"},
                "sender_channel_name": self.channel_name,
            }
        )

        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        # print("断开了")
        # 从组的连接计数中移除
        if self.channel_name in room_people_count.get(self.group_name, set()):
            room_people_count[self.group_name].remove(self.channel_name)

        # 如果组没有连接，移除该组
        if not room_people_count[self.group_name]:
            del room_people_count[self.group_name]

        raise StopConsumer()


admin_doctor_count = {}


class DoctorMessageList(AsyncWebsocketConsumer):
    def __init__(self):
        super().__init__()
        self.group_name = None

    async def websocket_connect(self, message):
        await self.accept()
        self.group_name = self.scope['url_route']['kwargs'].get('doctorID')
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        # 初始化组的连接计数
        if self.group_name not in admin_doctor_count:
            admin_doctor_count[self.group_name] = set()
        admin_doctor_count[self.group_name].add(self.channel_name)

    async def websocket_receive(self, message):
        group = self.group_name
        connection_count = len(admin_doctor_count.get(self.group_name, set()))
        if connection_count <= 1:
            await self.send(text_data=json.dumps({'status': 'false'}))
        else:
            await self.channel_layer.group_send(
                group,
                {
                    "type": "chat.message",
                    "message": message,
                    "sender_channel_name": self.channel_name,
                }
            )

    async def chat_message(self, event):
        message = event['message']['text']
        sender_channel_name = event['sender_channel_name']
        if self.channel_name != sender_channel_name:
            await self.send(text_data=message)

    async def websocket_disconnect(self, message):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        # print("断开了")
        # 从组的连接计数中移除
        if self.channel_name in admin_doctor_count.get(self.group_name, set()):
            admin_doctor_count[self.group_name].remove(self.channel_name)

        # 如果组没有连接，移除该组
        if not admin_doctor_count[self.group_name]:
            del admin_doctor_count[self.group_name]

        raise StopConsumer()


class AdminMessageList(AsyncWebsocketConsumer):
    def __init__(self):
        super().__init__()

    async def websocket_connect(self, message):
        await self.accept()
        self.group_name = 'admin-manage'
        await self.channel_layer.group_add(self.group_name, self.channel_name)

    async def websocket_receive(self, message):
        group = self.group_name
        await self.channel_layer.group_send(
            group,
            {
                "type": "chat.message",
                "message": message,
                "sender_channel_name": self.channel_name,
            }
        )

    async def chat_message(self, event):
        message = event['message']['text']
        sender_channel_name = event['sender_channel_name']
        if self.channel_name != sender_channel_name:
            await self.send(text_data=message)

    async def websocket_disconnect(self, message):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        raise StopConsumer()


user_doctor_count = {}


class UserMessageList(AsyncWebsocketConsumer):

    def __init__(self):
        super().__init__()

    async def websocket_connect(self, message):
        await self.accept()
        self.group_name = self.scope['url_route']['kwargs'].get('userID')
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        # 初始化组的连接计数
        if self.group_name not in user_doctor_count:
            user_doctor_count[self.group_name] = set()
        user_doctor_count[self.group_name].add(self.channel_name)

    async def websocket_receive(self, message):
        group = self.group_name
        connection_count = len(user_doctor_count.get(self.group_name, set()))
        # print(connection_count)
        if connection_count <= 1:
            await self.send(text_data=json.dumps({'status': 'false'}))
        else:
            await self.channel_layer.group_send(
                group,
                {
                    "type": "chat.message",
                    "message": message,
                    "sender_channel_name": self.channel_name,
                }
            )

    async def chat_message(self, event):
        message = event['message']['text']
        sender_channel_name = event['sender_channel_name']
        if self.channel_name != sender_channel_name:
            await self.send(text_data=message)

    async def websocket_disconnect(self, message):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        # 从组的连接计数中移除
        if self.channel_name in user_doctor_count.get(self.group_name, set()):
            user_doctor_count[self.group_name].remove(self.channel_name)

        # 如果组没有连接，移除该组
        if not user_doctor_count[self.group_name]:
            del user_doctor_count[self.group_name]

        raise StopConsumer()


class Pharmacy(AsyncWebsocketConsumer):
    def __init__(self):
        super().__init__()

    async def websocket_connect(self, message):
        await self.accept()
        self.group_name = 'pharmacy'
        await self.channel_layer.group_add(self.group_name, self.channel_name)

    async def websocket_receive(self, message):
        group = self.group_name
        await self.channel_layer.group_send(
            group,
            {
                "type": "chat.message",
                "message": message,
                "sender_channel_name": self.channel_name,
            }
        )

    async def chat_message(self, event):
        message = event['message']['text']
        sender_channel_name = event['sender_channel_name']
        if self.channel_name != sender_channel_name:
            await self.send(text_data=message)

    async def websocket_disconnect(self, message):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        raise StopConsumer()
