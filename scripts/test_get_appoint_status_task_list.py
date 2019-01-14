import json
import unittest
import requests
from base.base_action import get_url, get_params, get_res, get_token, start_log, params_log, res_log, end_log, now_time, \
    runtime, assert_equal
from base.logger import Log


class TestGetAppointStatusTaskList(unittest.TestCase):

    url = get_url('data', 'get_appoint_status_task_list', 'url')
    params = get_params('data', 'get_appoint_status_task_list', 'params')
    res = get_res('data', 'get_appoint_status_task_list', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('获取指定状态的任务列表接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_get_appoint_status_task_list(self):
        u"""获取指定状态的任务列表接口"""
        userToken = get_token()
        logger.info('获取token')
        new_params = dict(userToken, **self.params)
        logger.warning(params_log + str(new_params))
        r = requests.post(self.url, new_params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
