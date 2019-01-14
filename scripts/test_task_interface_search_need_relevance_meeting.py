import json
import unittest
import requests
from base.base_action import get_url, get_token, get_res, start_log, params_log, res_log, end_log, now_time, runtime, \
    assert_equal
from base.logger import Log


class TestTaskInterfaceSearchNeedRelevanceMeeting(unittest.TestCase):
    url = get_url('data', 'task_interface_search_need_relevance_meeting', 'url')
    res = get_res('data', 'task_interface_search_need_relevance_meeting', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('任务界面查询需要关联的会议接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_task_interface_search_need_relevance_meeting(self):
        u"""任务界面查询需要关联的会议接口"""
        params = get_token()
        logger.warning(params_log + str(params))
        r = requests.post(self.url, params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
