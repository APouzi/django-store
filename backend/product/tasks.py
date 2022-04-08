# Task delegation goes here. Need to install Homebrew and all that chippa!
from celery import shared_task
from django.core.mail import send_mail



@shared_task
def add_this(x,y):
    send_mail("Email from Django","This email is the email we get from django","alexandrepouzikov@gmail.com",["alexandrepouzikov@gmail.com"], fail_silently=True)
    print("This is a test")
    

@shared_task
def printPeriod():
    print("This is a test")
    

    