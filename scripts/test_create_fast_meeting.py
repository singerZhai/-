import unittest
import requests
from base.base_action import get_url, get_params, get_res, get_token, end_meeting


class TestCreateFastMeeting(unittest.TestCase):

    url = get_url('data', 'create_fast_meeting', 'url')
    params = get_params('data', 'create_fast_meeting', 'params')
    res = get_res('data', 'create_fast_meeting', 'res')
    end_meeting_url = get_url('data', 'end_meeting', 'url')

    def test_create_fast_meeting(self):
        u"""创建快速会议接口"""
        meetingId_dict = dict()
        user_token = get_token()
        new_params = dict(self.params, **user_token)
        r = requests.post(self.url, new_params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
        result = res['data']['meeting']['meetingId']
        meetingId_dict['meetingId'] = result
        end_meeting(meetingId_dict)
        result = res['data']['meetingId']['meetingId']
        meetingId_dict['meetingId'] = result
        end_meeting(meetingId_dict)
