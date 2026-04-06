from django.urls import path
from .views import UserView, HelloWorldView

urlpatterns = [
    path('users/', UserView.as_view()),
    path('', HelloWorldView.as_view()),
]