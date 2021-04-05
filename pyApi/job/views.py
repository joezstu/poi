import json
import os
from collections import OrderedDict
from pyexcel_xlsxw import save_data
from django.http import JsonResponse
import logging
from django.core.cache import cache

logger = logging.getLogger('django')


# Create your views here.
def downloadExcel(request):
    cookies = request.COOKIES.get('csrftoken')
    job_name = cookies[0:6]

    # 处理进度百分比
    total = cache.get(job_name + '-total')
    progress = cache.get(job_name + '-job')
    percent = int(progress * 100 / total)

    # 是否生成处理后的excel文件保存在服务器
    new_excel = cache.get(job_name + '-new')
    has_file = os.path.exists('upload/' + new_excel)

    if percent == 100:
        arr = cache.keys(job_name + '_*')
        arr = cache.get_many(arr)
        data = []
        for index, value in arr.items():
            value = json.loads(value)
            data.append(value)

        data2 = OrderedDict()
        data2.update({
            'sheet1': data
        })
        save_data('upload/' + new_excel, data)

    if has_file:
        has_file = True

    return JsonResponse({
        'percent': percent,
        'has_file': has_file,
        'fileName': cache.get(job_name + '-file'),
        'recordTotal': cache.get(job_name + '-total'),
        'recordHandle': cache.get(job_name + '-job'),
        'successRecord': cache.get(job_name + '-success'),
        'errorRecord': cache.get(job_name + '-error'),
        'handlePercent': int(cache.get(job_name + '-success') * 100 / cache.get(job_name + '-total')),

    })
