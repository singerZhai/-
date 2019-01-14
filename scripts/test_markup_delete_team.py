import unittest
import requests
import json
from base.base_action import get_url, get_res, now_time, start_log, runtime, end_log, get_team_id, params_log, res_log, \
    assert_equal, create_team
from base.logger import Log


class TestMarkupDeleteTeam(unittest.TestCase):

    url = get_url('data', 'markup_delete_team', 'url')
    res = get_res('data', 'markup_delete_team', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('标记删除团队接口(回收团队会议室号)')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_markup_delete_team(self):
        u"""标记删除团队接口(回收团队会议室号)"""
        create_team()
        teamId = get_team_id()
        logger.warning(params_log + str(teamId))
        r = requests.post(url=self.url, data=teamId)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
