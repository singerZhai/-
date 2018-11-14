import unittest
import requests
from base.base_action import get_url, get_res, get_token


class TestSearchUserMsg(unittest.TestCase):

    search_user_msg_url = get_url('data', 'search_user_msg', 'url')
    search_user_msg_res = get_res('data', 'search_user_msg', 'res')

    def test_search_user_msg(self):
        u"""查询用户信息接口"""
        user_token = get_token()
        r = requests.post(self.search_user_msg_url, user_token)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.search_user_msg_res['status'])
        self.assertEqual(res['msg'], self.search_user_msg_res['msg'])
