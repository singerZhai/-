import unittest
import requests
import json
from base.base_action import get_url, get_res, now_time, start_log, runtime, end_log, get_token, params_log, res_log, \
    assert_equal
from base.logger import Log


class TestSelectTeamList(unittest.TestCase):

    url = get_url('data', 'select_team_list', 'url')
    res = get_res('data', 'select_team_list', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('查询用户团队列表接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_select_team_list(self):
        u"""查询用户团队列表接口"""
        userToken = get_token()
        logger.warning(params_log + str(userToken))
        r = requests.post(url=self.url, data=userToken)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
