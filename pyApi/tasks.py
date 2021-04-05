import django
import os
from celery import Celery
import json

from django.http import JsonResponse
from django.core.cache import cache
import requests
import logging

logger = logging.getLogger('django')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyApi.settings')
django.setup()
app = Celery('handle_data', broker='redis://localhost:6379/')


@app.task
def handle_data(job_name, index, list):
    # cache缓存时间
    cache_time = 24 * 60 * 60

    # 初始化list
    list.append('')
    list.append('')

    # 从Redis获取要进行处理的数据
    cache.incr(job_name + '-job')

    key = "dbf94e0e96e4f52f06fb9ce1a1ffd951"
    keywords = list[22]

    # 对参数进行特殊字符处理
    # keywords = keywords.replace('(', '\\(')
    # keywords = keywords.replace(')', '\\)')
    index_l = keywords.find('(')
    index_r = keywords.find(')') + 1
    keywords = keywords.replace(keywords[index_l:index_r], '')
    print(8888888888888, keywords)

    # 关键词搜索API
    url = "https://restapi.amap.com/v3/place/text?key=" + key + "&keywords=" + keywords + "&extensions=all"
    res = requests.get(url)

    if res.status_code == 200:
        # 对返回数据进行json格式转换
        res = res.text
        res = json.loads(res)

        if not res['pois']:
            cache.incr(job_name + '-error')
            logger.info('地址："' + keywords + '"的关键词API返回的数据没有参考地址')
        else:
            address_object = res['pois'][0]
            location = address_object['location']
            reference_address = str(address_object['pname']) + str(address_object['cityname']) + str(
                address_object['adname']) + str(address_object['address'])
            # 更新记录的参考地址
            list[25] = reference_address

            # 周边搜索API
            url2 = "https://restapi.amap.com/v3/place/around?key=" + key + "&location=" + location + "&radius=10000&keywords=工商银行&sortrule=distance&offset=10&page=1";
            res2 = requests.get(url2)
            if res2.status_code == 200:
                res2 = res2.text
                res2 = json.loads(res2)
                data = res2['pois']
                if not data:
                    cache.incr(job_name + '-error')
                    logger.info('地址："' + keywords + '"的周边搜索API默认第一个地址周边没有工商银行')
                else:
                    cache.incr(job_name + '-success')
                    data_str = ''
                    for poi in data:

                        if poi['name']:
                            data_str += poi['name'] + '-'
                        if 'address' in poi:
                            if poi['address']:
                                try:
                                    data_str += poi['address'] + '-'
                                except IOError:
                                    logger.info('周边搜索API返回的银行地址不是字符串且非空的数据')

                        else:
                            logger.info('地址："' + keywords + '"的周边搜索API返回的银行地址没有address字段')

                        if poi['distance']:
                            data_str += poi['distance'] + '米,'

                    #         更新记录的返回数据
                    list[26] = data_str

            else:
                cache.incr(job_name + '-error')
                logger.info('地址："' + keywords + '"的周边搜索API获取失败,状态码=' + str(res.status_code))

    else:
        logger.info('地址："' + keywords + '"的关键词API获取失败,状态码=' + str(res.status_code))

    cache.set(job_name + '_' + str(index), json.dumps(list), cache_time)

    return JsonResponse({'name': 988})
