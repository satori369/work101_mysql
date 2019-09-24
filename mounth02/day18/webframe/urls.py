"""
声明客户端能够请求的数据
"""
from views import *

# 表达了能够处理的请求列表
urls = [
    ('/time',show_time),
    ('/guonei',guonei),
    ('/guoji,',guoji)
]