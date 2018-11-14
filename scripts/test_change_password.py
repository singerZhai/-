from time import sleep
import requests
import unittest
from base.base_action import get_url, get_params, get_token, get_res, change_back_password_params, again_change_password


class TestChangePassword(unittest.TestCase):

    change_url = get_url('data', 'change_password', 'url')
    change_params = get_params('data', 'change_password', 'params')
    change_res = get_res('data', 'change_password', 'res')
    change_back_password_params = change_back_password_params()

    def test_change_password(self):
        u"""修改密码接口"""
        userToken = get_token()
        # 拼接两个字典
        new_params = dict(self.change_params, **userToken)
        r = requests.post(self.change_url, new_params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.change_res['status'])
        self.assertEqual(res['msg'], self.change_res['msg'])
        # sleep作用：解决频繁调用接口报错问题
        sleep(3)
        # 将更改后密码再次更改回123456，使case能够正常执行
        again_change_password()
        # sleep作用：解决频繁调用接口报错问题
        sleep(3)
