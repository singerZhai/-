import unittest
import requests
import json
from base.base_action import get_url, get_params, get_res, get_team_id, get_token, now_time, start_log, runtime, \
    end_log, params_log, res_log, assert_equal
from base.logger import Log


class TestCreateSeatOrder(unittest.TestCase):

    url = get_url('data', 'create_seat_order', 'url')
    params = get_params('data', 'create_seat_order', 'params')
    res = get_res('data', 'create_seat_order', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('创建购买席位订单的接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    # 此装饰器为unitest中的标记预期失败
    @unittest.expectedFailure
    def test_create_seat_order(self):
        u"""创建购买席位订单的接口"""
        teamId = get_team_id()
        userToken = get_token()
        new_params = dict(userToken, **teamId, **self.params)
        logger.info(params_log + str(new_params))
        r = requests.post(url=self.url, data=new_params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
