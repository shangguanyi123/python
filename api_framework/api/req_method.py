#encoding=utf-8
import requests,json
from API_case.API_data import Config

class UserAPI:
    # {route} 接口路径
    @staticmethod
    def get(route):#get请求
        url = f"{Config.api_host}{route}"
        response = requests.get(url=url, headers=Config.headers)
        return response

    @staticmethod
    def post(route,data):#post请求 传json
        url = f"{Config.api_host}{route}"
        response = requests.post(url=url, headers=Config.headers_json, data=json.dumps(data))
        return response

    @staticmethod
    def post_biaodan(route, data):  # post请求 传表单
        url = f"{Config.api_host}{route}"
        response = requests.post(url=url, headers=Config.headers, data=data)
        return response

    @staticmethod
    def put(route, data):#put请求
        url = f"{Config.api_host}{route}"
        response = requests.put(url=url, headers=Config.headers_json, data=json.dumps(data))
        return response

    @staticmethod
    def delete(route):#delete请求
        url = f"{Config.api_host}{route}"
        response = requests.delete(url=url, headers=Config.headers)
        return response

