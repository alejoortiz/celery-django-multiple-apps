# Create your tasks here

from proj.celery import app
from packages.delay import delay_request


@app.task(queue='app')
def async_test_web():
    delay_request()
    return True
