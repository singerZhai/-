import unittest
import requests
from base.base_action import get_url, get_res, get_meeting_id_with_create_fast_meeting, get_token, start_log, \
    params_log, res_log, end_log, now_time, runtime, assert_equal
from base.logger import Log


class TestEndAppointMeeting(unittest.TestCase):

    url = get_url('data', 'end_appoint_meeting', 'url')
    res = get_res('data', 'end_appoint_meeting', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('结束指定的会议记录接口（只能结束自己创建的进行中的会议）')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_end_appoint_meeting(self):
        u"""结束指定的会议记录（只能结束自己创建的进行中的会议）"""
        # 先创建会议，然后用meetingId变量接收返回的meetingId
        meetingId_dict = get_meeting_id_with_create_fast_meeting()
        logger.info('创建会议并获取meetingId')
        userToken = get_token()
        logger.info('获取token')
        params = dict(userToken, **meetingId_dict)
        logger.info(params_log + str(params))
        r = requests.post(self.url, params)
        res = r.json()
        logger.info(res_log + str(res))
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
