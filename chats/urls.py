from django.urls import path

from . import views

app_name = "chats"

urlpatterns = [
    path("", views.index, name="index"),
    path("rooms/", views.rooms, name="rooms"),
    path("<str:room_name>/", views.room, name="room"),
    path("create/", views.create, name='create'),
]