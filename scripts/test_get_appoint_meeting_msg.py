import unittest
import requests
from base.base_action import get_url, get_res, get_meeting_id


class TestGetAppointMeetingMsg(unittest.TestCase):

    url = get_url('data', 'get_appoint_meeting_msg', 'url')
    res = get_res('data', 'get_appoint_meeting_msg', 'res')

    def test_get_appoint_meeting_msg(self):
        u"""获取指定会议的详细信息接口"""
        params = get_meeting_id()
        r = requests.post(self.url, params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
