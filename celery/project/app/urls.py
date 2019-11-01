from django.urls import path
from .views import send_mail_view, set_date

urlpatterns = [
    path('send-mail/', send_mail_view, name='send_mail'),
    path('create-task/', set_date, name='send_mail'),
]