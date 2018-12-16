import json
import unittest
import requests
from base.base_action import get_url, get_params, get_res, now_time, start_log, runtime, end_log, res_log, assert_equal
from base.logger import Log


class TestSelectByFromUsername(unittest.TestCase):

    url = get_url('data', 'select_by_from_username', 'url')
    params = get_params('data', 'select_by_from_username', 'params')
    res = get_res('data', 'select_by_from_username', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('群组列表查询接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_select_by_from_username(self):
        u"""群组列表查询接口"""
        r = requests.post(self.url, data=self.params)
        logger.info('进行接口请求')
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.info(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
