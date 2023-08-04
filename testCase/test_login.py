"""
=========================
Time    : 2023/8/4 11:20
Author  : Rowrey
Email   : ll1106@163.com
File    : test_login.py
=========================
"""
import pytest,allure,os

from libs.login import Login
from utils.handle_excel import get_excel_data
from common.baseApi import BaseAssert
from utils.handle_path import report_path

class TestLogin(BaseAssert):
    @pytest.mark.parametrize('inBody,expData',
                             get_excel_data('../data/Delivery_System_V1.0.xls','登录','Login','请求参数','响应预期结果'))
    def test_login(self,inBody,expData):
        # 调用业务层封装的代码
        res = Login().login(inBody)
        # 断言实际返回与预期结果
        self.define_assert(res['data']['msg'], expData['data']['msg'])

if __name__ == '__main__':
    pytest.main(['test_login.py','-s','--alluredir',report_path,'--clean-alluredir'])
    os.system(f'allure serve {report_path}')