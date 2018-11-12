import unittest
import requests
from base.base_action import get_url, get_params, get_res


class TestSignInDeviceUser(unittest.TestCase):

    url = get_url('data', 'sign_in_device_user', 'url')
    params = get_params('data', 'sign_in_device_user', 'params')
    res = get_res('data', 'sign_in_device_user', 'res')

    def test_sign_in_device_user(self):
        u"注册设备用户接口"
        r = requests.post(self.url, self.params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
