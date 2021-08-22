from django.http import HttpResponse

# Create your views here.
from web.task import async_test_web

def main(request):
    async_test_web.delay()
    return HttpResponse('Hello, World Web!')
