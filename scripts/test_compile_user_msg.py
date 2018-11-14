import unittest
import requests
from base.base_action import get_url, get_params, get_token, get_res


class TestCompileUserMsg(unittest.TestCase):
    url = get_url('data', 'compile_user_msg', 'url')
    params = get_params('data', 'compile_user_msg', 'params')
    res = get_res('data', 'compile_user_msg', 'res')

    def test_compile_user_msg(self):
        u"""编辑用户信息接口"""
        userToken = get_token()
        new_params = dict(self.params, **userToken)
        r = requests.post(self.url, new_params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
