from django.urls import include, path

from ChatnGo.api import views as app_views

urlpatterns = [
    path("users", app_views.UserList.as_view()),
    path("user/<int:pk>", app_views.UserDetail.as_view()),
    path("messages", app_views.MessageList.as_view()),
    path("messages/<int:pk>", app_views.MessageDetail.as_view()),
    path("rooms", app_views.ChatRoomList.as_view()),
    path("room/<int:pk>", app_views.ChatRoomDetail.as_view()),
]
