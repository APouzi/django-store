from celery import shared_task

@shared_task
def printThis(x,y):
    print(x,y)
    return x+y