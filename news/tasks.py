from celery import shared_task
import time

from django.core.mail import send_mail


@shared_task
def printer():
    send_mail(
        subject=f"Новости за прошедшую неделю",
        message=f"Здравствуй, username !",
        from_email='airat.s86@yandex.ru',
        recipient_list=[''],
    )
