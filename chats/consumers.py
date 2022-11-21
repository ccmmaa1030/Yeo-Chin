import json

from accounts.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import Room, Message
from django.contrib.humanize.templatetags.humanize import naturaltime
import datetime

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chats_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json['username'] #
        room = text_data_json['room'] #
        date_added = text_data_json['date_added'] #
        if message:
            await self.save_message(username, room, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message, 'username': username, 'date_added': date_added}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        username = event['username']
        date_added = event['date_added']
        print(date_added)
        new_date_added = datetime.datetime.strptime(date_added.split('.')[0].replace('T', ' '), '%Y-%m-%d %H:%M:%S')
        kr_date_added = new_date_added + datetime.timedelta(hours=9)
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, 'username': username, 'date_added': naturaltime(kr_date_added)}))

    @sync_to_async
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(name=room)
        print('성공')
        Message.objects.create(user=user, room=room, content=message)
        print('성공')