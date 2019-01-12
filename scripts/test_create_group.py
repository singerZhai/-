import json

import requests
import unittest

from base.base_action import get_url, get_params, get_res, now_time, start_log, runtime, end_log, params_log, res_log, \
    assert_equal
from base.logger import Log


class TestCreateGroup(unittest.TestCase):

    url = get_url('data', 'create_group', 'url')
    params = get_params('data', 'create_group', 'params')
    res = get_res('data', 'create_group', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('创建群组接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_create_group(self):
        u"""创建群组接口"""
        logger.info(params_log + str(self.params))
        r = requests.post(self.url, data=self.params)
        logger.info('进行接口请求')
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
