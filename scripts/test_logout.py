from time import sleep

import allure
import requests
import pytest
from base.base_action import get_url, get_res, get_token


class TestLogout:
    # 用户退出接口
    @allure.step('用户退出接口测试')
    def test_logout(self):
        while True:
            logout_url = get_url('data', 'logout', 'url')
            logout_res = get_res('data', 'logout', 'res')
            user_token = get_token()
            sleep(3)
            r = requests.post(logout_url, user_token)
            res = r.json()
            if res['status'] == 200:
                assert res['status'] == logout_res['status']
                assert res['msg'] == logout_res['msg']
                return
            elif res['status'] == 0:
                print('此次返回码为:%d, 预期为:%d' % (res['status'], logout_res['status']))
                print('此次返回msg为:%s, 预期为:%s' % (res['msg'], logout_res['msg']))
                self.test_logout()
