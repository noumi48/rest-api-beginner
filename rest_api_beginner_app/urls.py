from django.urls import path
from rest_api_beginner_app import views

urlpatterns = [
    path('hello-api/', views.HelloApiView.as_view()),
]