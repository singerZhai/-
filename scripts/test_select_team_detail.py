import unittest
import requests
import json
from base.base_action import get_url, get_res, now_time, start_log, runtime, end_log, get_team_id, params_log, res_log, \
    assert_equal
from base.logger import Log


class TestSelectTeamDetail(unittest.TestCase):

    url = get_url('data', 'select_team_detail', 'url')
    res = get_res('data', 'select_team_detail', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('查询团队详情接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_select_team_detail(self):
        u"""查询团队详情接口"""
        teamId = get_team_id()
        logger.info(params_log + str(teamId))
        r = requests.post(url=self.url, data=teamId)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
