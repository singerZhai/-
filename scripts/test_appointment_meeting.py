import json
import unittest
import requests
from base.logger import Log
from base.base_action import get_url, get_params, get_res, get_meeting_start_time, get_meeting_end_time, get_token, \
    get_appointment_meetingId, end_meeting, select_appointment_meeting_msg, params_log, res_log, start_log, end_log, \
    now_time, runtime, end_meeting_log, assert_equal


class TestAppointmentMeeting(unittest.TestCase):

    url = get_url('data', 'appointment_meeting', 'url')
    params = get_params('data', 'appointment_meeting', 'params')
    preBeginTime = get_meeting_start_time()
    preEndTime = get_meeting_end_time()
    res = get_res('data', 'appointment_meeting', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('预约会议接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_appointment_meeting(self):
        u"""预约会议接口"""
        user_token = get_token()
        logger.info('获取token')
        new_params = dict(self.params, **self.preBeginTime, **self.preEndTime, **user_token)
        logger.warning(params_log + str(new_params))
        r = requests.post(self.url, new_params)
        logger.info('进行接口请求')
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
        appointment_meeting_msg = select_appointment_meeting_msg()
        meetingId = get_appointment_meetingId(appointment_meeting_msg)
        end_meeting(meetingId)
        logger.info(end_meeting_log)