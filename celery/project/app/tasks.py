from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from celery.decorators import periodic_task
from celery.task.schedules import crontab


@shared_task
def sum(a=2, b=4):
    return a+b

@shared_task
def email(text=""):
    pass