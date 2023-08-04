"""
=========================
Time    : 2023/8/3 13:42
Author  : Rowrey
Email   : ll1106@163.com
File    : baseApi.py
=========================
"""
import inspect

import requests
from utils.handle_yaml import get_yaml_data
from configs.config import HOST

class BaseApi:
    def __init__(self,token=None):
        if token:
            self.header = {'Authorization': token}
        else:
            self.header = None
        # 通过类名作为键去获取对应类的数据
        # 获取继承 BaseApi 的子类的类名 self.__class__.__name__
        self.data = get_yaml_data('../data/apiConfig.yaml')[self.__class__.__name__]
    def request_send(self,inData):
        try:
            funcName = inspect.stack()[1][3]
            data = self.data[funcName]
            res = requests.request(method=data['method'],url=f'{HOST}'+data['url'],params=inData,headers=self.header)
            # res = requests.request(method=data['method'],url=f'{HOST}'+data['url'],params=inData)
            print(str(res))
            return res.json()
        except Exception as error:
            raise error

#-------断言类 封装 -------
class BaseAssert:
    @classmethod # 使用类名就直接可以调用类方法
    def define_assert(cls,res,expData):
        try:
            assert res == expData
        except Exception as error:
            raise error

