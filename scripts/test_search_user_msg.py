import json
import unittest
import requests
from base.base_action import get_url, get_res, get_token, start_log, res_log, end_log, now_time, runtime, assert_equal
from base.logger import Log


class TestSearchUserMsg(unittest.TestCase):

    url = get_url('data', 'search_user_msg', 'url')
    res = get_res('data', 'search_user_msg', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('查询用户信息接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_search_user_msg(self):
        u"""查询用户信息接口"""
        user_token = get_token()
        logger.info('获取token')
        r = requests.post(self.url, user_token)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
