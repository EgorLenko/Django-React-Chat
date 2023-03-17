from .views import *

from django.urls import path

urlpatterns = [
    path('users', UserList.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),
    path('messages', MessageList.as_view()),
    path('messages/<int:pk>', MessageDetail.as_view()),
    path('rooms', ChatRoomList.as_view()),
    path('room/<int:pk>', ChatRoomDetail.as_view()),

]
