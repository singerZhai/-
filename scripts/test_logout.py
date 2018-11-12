import unittest
import requests
from base.base_action import get_url, get_res, get_token


class TestLogout(unittest.TestCase):
    logout_url = get_url('data', 'logout', 'url')
    logout_res = get_res('data', 'logout', 'res')

    def test_logout(self):
        u"用户退出接口"
        user_token = get_token()
        r = requests.post(self.logout_url, user_token)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.logout_res['status'])
        self.assertEqual(res['msg'], self.logout_res['msg'])
