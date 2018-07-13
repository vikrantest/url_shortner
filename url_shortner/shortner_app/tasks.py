import os
import time
from celery.decorators import task


@task
def temp():
	print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++123123123131')
	time.sleep(9)
	return 2+2