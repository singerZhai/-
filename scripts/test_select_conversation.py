import json
import unittest
import requests
from base.base_action import get_url, get_params, get_res, now_time, start_log, runtime, end_log, res_log, params_log, \
    assert_equal
from base.logger import Log


class TestSelectConversation(unittest.TestCase):

    url = get_url('data', 'select_conversation', 'url')
    params = get_params('data', 'select_conversation', 'params')
    res = get_res('data', 'select_conversation', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('会话查询接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_select_conversation(self):
        u"""会话查询接口"""
        logger.warning(params_log + str(self.params))
        r = requests.post(self.url, data=self.params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
