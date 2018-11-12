import unittest
import requests
from base.base_action import get_url, get_res, get_user_id


class TestLogoutDeviceUser(unittest.TestCase):

    url = get_url('data', 'logout_device_user', 'url')
    params = get_user_id()
    res = get_res('data', 'logout_device_user', 'res')

    def test_logout_device_user(self):
        u"注销设备用户"
        r = requests.post(self.url, self.params)
        r = requests.post(self.url, self.params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
