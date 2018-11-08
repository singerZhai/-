from time import sleep

import allure
import requests
import pytest
from base.base_action import get_url, get_res, get_token


class TestLogout:
    logout_url = get_url('data', 'logout', 'url')
    logout_res = get_res('data', 'logout', 'res')

    # 用户退出接口
    @allure.step('用户退出接口测试')
    def test_logout(self):
        user_token = get_token()
        r = requests.post(self.logout_url, user_token)
        res = r.json()
        assert res['status'] == self.logout_res['status']
        assert res['msg'] == self.logout_res['msg']
