from channels.generic.websocket import AsyncWebsocketConsumer
import json
from random import randint
from asyncio import sleep
from channels.exceptions import StopConsumer


class WSConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        await self.channel_layer.group_add("jokes", self.channel_name)
        await self.accept()
        print("Client is connected!")
        
    
    async def disconnect(self, close_code):
        print('disconnected! ', close_code)
        # Leave room group
        await self.channel_layer.group_discard("jokes", self.channel_name)
        raise StopConsumer()


    async def send_jokes(self, event):
        text_message = event['text'] # receive from celery (tasks.py)
        await self.send(text_message) # send to client
