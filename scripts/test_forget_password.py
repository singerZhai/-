import requests
import unittest
from base.base_action import get_url, get_params, get_res


class TestForgetPassword(unittest.TestCase):

    forget_url = get_url('data', 'forget_password', 'url')
    forget_params = get_params('data', 'forget_password', 'params')
    forget_res = get_res('data', 'forget_password', 'res')

    @unittest.skipIf(condition=True, reason='万能验证码')
    def test_forget_password(self):
        u"""用户忘记密码接口"""
        r = requests.post(self.forget_url, self.forget_params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.forget_res['status'])
        self.assertEqual(res['msg'], self.forget_res['msg'])
