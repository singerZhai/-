import unittest
import requests
from base.base_action import get_url, get_params, get_res, get_token


class TestMeetingStatusSearchWithMe(unittest.TestCase):

    url = get_url('data', 'meeting_status_search_with_me', 'url')
    params = get_params('data', 'meeting_status_search_with_me', 'params')
    res = get_res('data', 'meeting_status_search_with_me', 'res')

    def test_meeting_status_search_with_me(self):
        u"""根据会议状态的查询和我相关的会议接口"""
        usertoken = get_token()
        new_params = dict(self.params, **usertoken)
        r = requests.post(self.url, new_params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
