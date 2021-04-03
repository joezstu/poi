import json

from django.http import HttpResponse
from django.middleware.csrf import get_token


def token(request):
    cc = get_token(request)
    return HttpResponse(json.dumps({'token': cc}), content_type="application/json,charset=utf-8")
