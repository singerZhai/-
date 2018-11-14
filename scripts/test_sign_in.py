import unittest
import requests
from base.base_action import get_url, get_params, get_res


class TestSignIn(unittest.TestCase):

    sign_in_url = get_url('data', 'sign_in', 'url')
    sign_in_params = get_params('data', 'sign_in', 'params')
    sign_in_res = get_res('data', 'sign_in', 'res')

    @unittest.skipIf(condition=True, reason='万能验证码')
    def test_sign_in(self):
        u"""用户注册接口"""
        r = requests.post(self.sign_in_url, self.sign_in_params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.sign_in_res['status'])
        self.assertEqual(res['msg'], self.sign_in_res['msg'])
