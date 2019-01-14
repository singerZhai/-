import json
import unittest
import requests
from base.base_action import get_url, get_res, get_meeting_id_with_create_fast_meeting, end_meeting, start_log, \
    params_log, res_log, end_log, now_time, runtime, assert_equal
from base.logger import Log


class TestGetAppointMeetingMsg(unittest.TestCase):

    url = get_url('data', 'get_appoint_meeting_msg', 'url')
    res = get_res('data', 'get_appoint_meeting_msg', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('获取指定会议的详细信息接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_get_appoint_meeting_msg(self):
        u"""获取指定会议的详细信息接口"""
        meetingId_dict = dict()
        params = get_meeting_id_with_create_fast_meeting()
        logger.info('创建快速会议并获取meetingId')
        logger.warning(params_log + str(params))
        r = requests.post(self.url, params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
        result = res['data']['meeting']['meetingId']
        meetingId_dict['meetingId'] = result
        end_meeting(meetingId_dict)
        logger.info('结束会议')
