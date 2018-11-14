import unittest
import requests
from base.base_action import get_url, get_params, get_res, get_meeting_start_time, get_meeting_end_time, get_token


class TestAppointmentMeeting(unittest.TestCase):

    url = get_url('data', 'appointment_meeting', 'url')
    params = get_params('data', 'appointment_meeting', 'params')
    preBeginTime = get_meeting_start_time()
    preEndTime = get_meeting_end_time()
    res = get_res('data', 'appointment_meeting', 'res')

    def test_appointment_meeting(self):
        u"""预约会议接口"""
        user_token = get_token()
        new_params = dict(self.params, **self.preBeginTime, **self.preEndTime, **user_token)
        r = requests.post(self.url, new_params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
