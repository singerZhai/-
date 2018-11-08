import allure
import pytest
import requests
from base.base_action import get_url, get_res, get_params


class TestLogin:

    login_url = get_url('data', 'login', 'url')
    login_params = get_params('data', 'login', 'params')
    login_res = get_res('data', 'login', 'res')
    fast_login_url = get_url('data', 'fast_login', 'url')
    fast_login_params = get_params('data', 'fast_login', 'params')
    fast_login_res = get_res('data', 'fast_login', 'res')

    # 用户登录接口
    @allure.step('用户登录接口测试')
    def test_login(self):
        r = requests.post(self.login_url, self.login_params)
        res = r.json()
        assert res['status'] == self.login_res['status']
        assert res['msg'] == self.login_res['msg']

    # 快速登录接口
    @pytest.mark.skipif(condition=True, reason='万能验证码')
    @allure.step('用户登录接口测试')
    def test_fast_login(self):
        r = requests.post(self.fast_login_url, self.fast_login_params)
        res = r.json()
        print(res)
        assert res['status'] == self.fast_login_res['status']
        assert res['msg'] == self.fast_login_res['msg']
