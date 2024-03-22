from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'letter'

urlpatterns = [
	path('create/', LetterCreateView.as_view()),
	path('<int:pk>', LetterSend.as_view()),
    path('', LetterView.as_view(), name='list'),
    path('sended', SendMail, name='sended')
]
