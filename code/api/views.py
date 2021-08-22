from django.http import HttpResponse

# Create your views here.
from api.task import async_test_api

def main(request):
    async_test_api.delay()
    return HttpResponse('Hello, World API!')
