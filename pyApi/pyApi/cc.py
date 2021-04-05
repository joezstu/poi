from django.shortcuts import render

from django.http import HttpResponse
from django.core.cache import cache


def bc(request):
    cookies = request.COOKIES.get('csrftoken')
    job_name = cookies[0:6]

    return HttpResponse(cache.get(job_name+'-new'))
