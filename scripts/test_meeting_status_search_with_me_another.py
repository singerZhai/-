import json
import unittest
import requests
from base.base_action import get_url, get_params, get_res, get_token, start_log, params_log, res_log, end_log, now_time, \
    runtime, assert_equal
from base.logger import Log


class TestMeetingStatusSearchWithMeAnother(unittest.TestCase):

    url = get_url('data', 'meeting_status_search_with_me_another', 'url')
    params = get_params('data', 'meeting_status_search_with_me_another', 'params')
    res = get_res('data', 'meeting_status_search_with_me_another', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('根据会议状态的查询和我相关的会议接口(支持同时查询多种状态)')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_meeting_status_search_with_me_another(self):
        u"""根据会议状态的查询和我相关的会议接口(支持同时查询多种状态)"""
        usertoken = get_token()
        logger.info('获取token')
        new_params = dict(self.params, **usertoken)
        logger.info(params_log + str(new_params))
        r = requests.post(self.url, new_params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
