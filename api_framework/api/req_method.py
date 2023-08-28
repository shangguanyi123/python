#coding=gbk
import requests,json
from api_framework.API_case.API_data import Config

class UserAPI:
    # {route} �ӿ�·��
    @staticmethod
    def get(route):#get����
        url = f"{Config.api_host}{route}"
        response = requests.get(url=url, headers=Config.headers)
        assert response.status_code == 200
        return response

    @staticmethod
    def post(route,data):#post���� ��json
        url = f"{Config.api_host}{route}"
        response = requests.post(url=url, headers=Config.headers_json, data=json.dumps(data))
        assert response.status_code == 200
        return response

    @staticmethod
    def post_biaodan(route, data):  # post���� ����
        url = f"{Config.api_host}{route}"
        response = requests.post(url=url, headers=Config.headers_biaodan, data=data)
        assert response.status_code == 200
        return response

    @staticmethod
    def put(route, data):#put����
        url = f"{Config.api_host}{route}"
        response = requests.put(url=url, headers=Config.headers_json, data=json.dumps(data))
        assert response.status_code == 200
        return response

    @staticmethod
    def delete(route):#delete����
        url = f"{Config.api_host}{route}"
        response = requests.delete(url=url, headers=Config.headers)
        assert response.status_code == 200
        return response

