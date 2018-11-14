import unittest
from time import sleep
import requests
from base.base_action import get_url, get_params, get_res, sign_in_device_user


class TestTabletUserFastLogin(unittest.TestCase):

    url = get_url('data', 'tablet_user_fast_login', 'url')
    params = get_params('data', 'tablet_user_fast_login', 'params')
    res = get_res('data', 'tablet_user_fast_login', 'res')

    def test_tablet_user_fast_login(self):
        u"""平板用户快速登录接口"""
        # 先停1s，防止频繁调用接口
        sleep(1)
        r = requests.post(self.url, self.params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
