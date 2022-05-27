from . import views
from django.urls import path, include
app_name = 'room'
urlpatterns = [
    path('', views.room, name="room"),
    path('/<str:pk>/', views.detail, name="detail"),
    path('create-room/', views.createRoom, name="createroom"),
    path('update/<str:pk>/', views.updateRoom, name="update"),
    path('del/<str:pk>/', views.delRoom, name="del"),
    path('del-mess/<str:pk>/', views.delCMT, name="delmess"),
    path('room_topic/', views.topicRoom, name="topicRoom"),
]