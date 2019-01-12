import requests
import unittest
import json
from base.base_action import get_url, get_params, get_res, now_time, start_log, runtime, end_log, get_token, params_log, \
    res_log, assert_equal
from base.logger import Log


class TestLeaveMessage(unittest.TestCase):

    url = get_url('data', 'leave_message', 'url')
    params = get_params('data', 'leave_message', 'params')
    res = get_res('data', 'leave_message', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('发送意见接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_leave_message(self):
        u"""发送意见接口"""
        userToken = get_token()
        new_params = dict(userToken, **self.params)
        logger.info(params_log + str(new_params))
        r = requests.post(url=self.url, data=new_params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
