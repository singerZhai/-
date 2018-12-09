import unittest
import requests
from base.base_action import get_url, get_params, get_res, get_token, end_meeting, params_log, res_log, start_log, \
    end_log, now_time, runtime, assert_equal
from base.logger import Log


class TestCreateFastMeeting(unittest.TestCase):

    url = get_url('data', 'create_fast_meeting', 'url')
    params = get_params('data', 'create_fast_meeting', 'params')
    res = get_res('data', 'create_fast_meeting', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('创建快速会议接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_create_fast_meeting(self):
        u"""创建快速会议接口"""
        meetingId_dict = dict()
        user_token = get_token()
        logger.info('获取token')
        new_params = dict(self.params, **user_token)
        logger.info(params_log + str(new_params))
        r = requests.post(self.url, new_params)
        logger.info('创建快速会议')
        res = r.json()
        logger.info(res_log + str(res))
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
        result = res['data']['meetingId']['meetingId']
        meetingId_dict['meetingId'] = result
        logger.info('获取meetingId')
        end_meeting(meetingId_dict)
        logger.info('关闭会议')
