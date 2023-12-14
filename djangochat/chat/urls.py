from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<str:room>/", views.room, name="room"),
    path("checkview", views.checkview, name="checkview"),
    path("send", views.send, name="send"),
]