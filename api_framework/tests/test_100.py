import json
from website_api.ichempro_api import *


def test_01():
    res1 = Keshangguanli().sel_kuhu_bianma()
    print('获取客户编码',res1.json())