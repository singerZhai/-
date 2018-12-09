import unittest
import requests
from base.base_action import get_token, get_meeting_id_with_create_fast_meeting, get_url, get_res, start_log, \
    params_log, res_log, end_log, now_time, runtime, assert_equal
from base.logger import Log


class TestDeleteAppointmentMeetingRecord(unittest.TestCase):
    url = get_url('data', 'delete_appointment_meeting_record', 'url')
    res = get_res('data', 'delete_appointment_meeting_record', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('删除指定的会议记录接口（只能删除自己创建的预约中的会议）')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_delete_appointment_meeting_record(self):
        u"""删除指定的会议记录接口（只能删除自己创建的预约中的会议）"""
        meeting_id = get_meeting_id_with_create_fast_meeting()
        logger.info('创建快速会议并获取meetingId')
        user_token = get_token()
        logger.info('获取token')
        params = dict(user_token, **meeting_id)
        logger.info(params_log + str(params))
        r = requests.post(self.url, params)
        res = r.json()
        logger.info(res_log + str(res))
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
