import json
import unittest
import requests
from base.base_action import get_url, get_res, get_token, start_log, res_log, end_log, now_time, runtime, assert_equal
from base.logger import Log


class TestLogout(unittest.TestCase):
    url = get_url('data', 'logout', 'url')
    res = get_res('data', 'logout', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('用户退出接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_logout(self):
        u"""用户退出接口"""
        user_token = get_token()
        logger.info('获取token')
        r = requests.post(self.url, user_token)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.info(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
