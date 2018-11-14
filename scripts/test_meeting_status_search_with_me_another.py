import unittest
import requests
from base.base_action import get_url, get_params, get_res, get_token


class TestMeetingStatusSearchWithMeAnother(unittest.TestCase):

    url = get_url('data', 'meeting_status_search_with_me_another', 'url')
    params = get_params('data', 'meeting_status_search_with_me_another', 'params')
    res = get_res('data', 'meeting_status_search_with_me_another', 'res')

    def test_meeting_status_search_with_me_another(self):
        u"""根据会议状态的查询和我相关的会议接口(支持同时查询多种状态)"""
        usertoken = get_token()
        new_params = dict(self.params, **usertoken)
        r = requests.post(self.url, new_params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
