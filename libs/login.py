import hashlib
import copy
from configs.config import NAME_PASS
from common.baseApi import BaseApi

def get_md5_data(psw: str):
    #实例化一个MD5对象
    md5 = hashlib.md5()
    # 调用加密方法
    md5.update(psw.encode('utf-8'))
    return md5.hexdigest()
class Login(BaseApi):
    def login(self,inData,getToken=False):
        # 请求体
        inData = copy.copy(inData)# 浅拷贝
        #inData['password'] = get_md5_data(inData['password'])
        pyload = inData
        # 发送请求
        respData = self.request_send(pyload)
        if getToken:# 返回token
            return respData['data']['token']
        return respData#响应数据

if __name__ == '__main__':
    res = Login().login(NAME_PASS)
    print(res)
