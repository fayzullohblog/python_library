
from celery import shared_task
 
@shared_task(name='natija chiqazadi printdi')
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

import time
@shared_task(name='2 sondi quishish funtion')
def add(a,b):
    time.sleep(10)
    return a+b
