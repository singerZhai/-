import unittest
import requests
from base.base_action import get_url, get_params, get_res, get_token, start_log, params_log, res_log, end_log, now_time, \
    runtime, assert_equal
from base.logger import Log


class TestSelectTaskCopyToMe(unittest.TestCase):

    url = get_url('data', 'select_task_copy_to_me', 'url')
    params = get_params('data', 'select_task_copy_to_me', 'params')
    res = get_res('data', 'select_task_copy_to_me', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('查询抄送给我的任务接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_select_task_copy_to_me(self):
        u"""查询抄送给我的任务接口"""
        userToken = get_token()
        logger.info('获取token')
        new_params = dict(userToken, **self.params)
        logger.info(params_log + str(new_params))
        r = requests.post(self.url, new_params)
        res = r.json()
        logger.info(res_log + str(res))
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
