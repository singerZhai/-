import json
import unittest
import requests
from base.base_action import get_url, get_params, get_res, start_log, params_log, res_log, end_log, now_time, runtime, \
    assert_equal
from base.logger import Log


class TestTabletUserFastLogin(unittest.TestCase):

    url = get_url('data', 'tablet_user_fast_login', 'url')
    params = get_params('data', 'tablet_user_fast_login', 'params')
    res = get_res('data', 'tablet_user_fast_login', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('平板用户快速登录接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_tablet_user_fast_login(self):
        u"""平板用户快速登录接口"""
        logger.info(params_log + str(self.params))
        r = requests.post(self.url, self.params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.info(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
