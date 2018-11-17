import unittest
import requests
from base.base_action import get_url, get_res, get_meeting_id_with_create_fast_meeting, get_token


class TestEndAppointMeeting(unittest.TestCase):

    url = get_url('data', 'end_appoint_meeting', 'url')
    res = get_res('data', 'end_appoint_meeting', 'res')

    def test_end_appoint_meeting(self):
        u"""结束指定的会议记录（只能结束自己创建的进行中的会议）"""
        # 先创建会议，然后用meetingId变量接收返回的meetingId
        meetingId_dict = get_meeting_id_with_create_fast_meeting()
        userToken = get_token()
        params = dict(userToken, **meetingId_dict)
        r = requests.post(self.url, params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
