import unittest
import requests
from base.logger import Log
from base.base_action import get_url, get_params, get_res, get_meeting_start_time, get_meeting_end_time, get_token, \
    get_appointment_meetingId, end_meeting, select_appointment_meeting_msg, params_log, res_log


class TestAppointmentMeeting(unittest.TestCase):
    url = get_url('data', 'appointment_meeting', 'url')
    params = get_params('data', 'appointment_meeting', 'params')
    preBeginTime = get_meeting_start_time()
    preEndTime = get_meeting_end_time()
    res = get_res('data', 'appointment_meeting', 'res')

    def test_appointment_meeting(self):
        u"""预约会议接口"""
        logger = Log()
        user_token = get_token()
        new_params = dict(self.params, **self.preBeginTime, **self.preEndTime, **user_token)
        logger.info(params_log + str(new_params))
        r = requests.post(self.url, new_params)
        res = r.json()
        logger.info(res_log + str(res))
        # print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
        appointment_meeting_msg = select_appointment_meeting_msg()
        meetingId = get_appointment_meetingId(appointment_meeting_msg)
        end_meeting(meetingId)
        logger.info('会议已结束')