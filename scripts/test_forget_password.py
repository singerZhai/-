import requests
import unittest
from base.base_action import get_url, get_params, get_res, start_log, params_log, res_log, end_log, now_time, runtime, \
    assert_equal
from base.logger import Log


class TestForgetPassword(unittest.TestCase):

    url = get_url('data', 'forget_password', 'url')
    params = get_params('data', 'forget_password', 'params')
    res = get_res('data', 'forget_password', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('用户忘记密码接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    @unittest.skipIf(condition=True, reason='万能验证码')
    def test_forget_password(self):
        u"""用户忘记密码接口"""
        logger.info(params_log + str(self.params))
        r = requests.post(self.url, self.params)
        res = r.json()
        logger.info(res_log + str(res))
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
