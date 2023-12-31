from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/chat/room/', consumers.p5Consumer),
    path('ws/chat/snake/', consumers.snakeConsumer.as_asgi()),
    path('ws/chat/<room_name>/', consumers.ChatConsumer),
]