from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from django.core.cache import cache
import time
from tasks import handle_data


@require_http_methods(["POST"])
def import_excel(request):

    handle = request.FILES['excel_file']
    # 定义任务名
    cookies = request.COOKIES.get('csrftoken')
    job_name = cookies[0:6]

    # 清空缓存
    cache.delete_pattern(job_name+'*')

    arr = handle.get_array()

    # cache缓存时间
    cache_time: int = 24 * 60 * 60

    # 文件名
    cache.set(job_name + '-file', handle.name, cache_time)
    # 处理后的文件名，包括路径（相对根目录）
    cache.set(job_name + '-new', job_name + '_' + time.strftime('%Y%m%d%H%M%S') + '.xls', cache_time)
    # excel文件总记录数
    cache.set(job_name + '-total', len(arr), cache_time)
    # 成功获取数据的记录数
    cache.set(job_name + '-success', 0, cache_time)
    # 没有获取数据的记录数
    cache.set(job_name + '-error', 0, cache_time)
    # 成功处理任务数量
    cache.set(job_name + '-job', 0, cache_time)

    for index, value in enumerate(arr):
        handle_data.delay(job_name, index, value)

    return JsonResponse({})
