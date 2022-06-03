from . import views
from django.urls import path, include
app_name = 'user'
urlpatterns = [
    path('', views.user, name="user"),
    path('pro/<str:pk>/', views.profile, name="profile"),
]