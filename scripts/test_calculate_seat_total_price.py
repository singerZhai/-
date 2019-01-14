import unittest
import requests
import json
from base.base_action import get_url, get_params, get_res, now_time, start_log, runtime, end_log, params_log, res_log, \
    assert_equal
from base.logger import Log


class TestCalculateSeatTotalPrice(unittest.TestCase):

    url = get_url('data', 'calculate_seat_total_price', 'url')
    params = get_params('data', 'calculate_seat_total_price', 'params')
    res = get_res('data', 'calculate_seat_total_price', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('席位总价计算接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_calculate_seat_total_price(self):
        u"""席位总价计算接口"""
        logger.warning(params_log + str(self.params))
        r = requests.post(url=self.url, data=self.params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
