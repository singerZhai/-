import unittest
import requests
from base.base_action import get_url, get_params, get_token, get_res, params_log, \
    res_log, start_log, end_log, now_time, runtime, assert_equal
from base.logger import Log


class TestCompileUserMsg(unittest.TestCase):
    url = get_url('data', 'compile_user_msg', 'url')
    params = get_params('data', 'compile_user_msg', 'params')
    res = get_res('data', 'compile_user_msg', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('编辑用户信息接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_compile_user_msg(self):
        u"""编辑用户信息接口"""
        userToken = get_token()
        logger.info('获取token')
        new_params = dict(self.params, **userToken)
        logger.info(params_log + str(new_params))
        r = requests.post(self.url, new_params)
        res = r.json()
        logger.info(res_log + str(res))
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
