import json
from time import sleep
import requests
import unittest
from base.base_action import get_url, get_params, get_token, get_res, change_back_password_params, \
    again_change_password, params_log, res_log, start_log, end_log, runtime, now_time, assert_equal
from base.logger import Log


class TestChangePassword(unittest.TestCase):

    url = get_url('data', 'change_password', 'url')
    params = get_params('data', 'change_password', 'params')
    res = get_res('data', 'change_password', 'res')
    change_back_password_params = change_back_password_params()

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('修改密码接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_change_password(self):
        u"""修改密码接口"""
        userToken = get_token()
        logger.info('获取token')
        # 拼接两个字典
        new_params = dict(self.params, **userToken)
        logger.info(params_log + str(new_params))
        r = requests.post(self.url, new_params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.info(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
        # sleep作用：解决频繁调用接口报错问题
        sleep(1)
        # 将更改后密码再次更改回123456，使case能够正常执行
        again_change_password()
        logger.info('将密码改回至123456')
        # sleep作用：解决频繁调用接口报错问题
        sleep(1)
