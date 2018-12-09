import unittest
import requests
from base.base_action import get_url, get_res, get_date, get_token, start_log, params_log, res_log, end_log, now_time, \
    runtime, assert_equal
from base.logger import Log


class TestSelectSchedule(unittest.TestCase):

    url = get_url('data', 'select_schedule', 'url')
    res = get_res('data', 'select_schedule', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('获取用户指定日期的日程列表接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_select_schedule(self):
        u"""获取用户指定日期的日程列表接口"""
        now_date = get_date()
        userToken = get_token()
        logger.info('获取token')
        params = dict(userToken, **now_date)
        logger.info(params_log + str(params))
        r = requests.post(self.url, params)
        res = r.json()
        logger.info(res_log + str(res))
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
