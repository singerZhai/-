import unittest
import requests
from base.base_action import get_token, get_meeting_id, get_url, get_res


class TestDeleteAppointmentMeetingRecord(unittest.TestCase):
    url = get_url('data', 'delete_appointment_meeting_record', 'url')
    res = get_res('data', 'delete_appointment_meeting_record', 'res')

    def test_delete_appointment_meeting_record(self):
        u"""删除指定的会议记录接口（只能删除自己创建的预约中的会议）"""
        meeting_id = get_meeting_id()
        user_token = get_token()
        params = dict(user_token, **meeting_id)
        print(params)
        r = requests.post(self.url, params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
