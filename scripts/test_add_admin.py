import unittest
import requests
import json
from base.base_action import get_url, get_params, get_res, now_time, start_log, runtime, end_log, create_team, \
    get_team_id, get_token, params_log, res_log, assert_equal, delete_team
from base.logger import Log


class TestAddAdmin(unittest.TestCase):

    url = get_url('data', 'add_admin', 'url')
    params = get_params('data', 'add_admin', 'params')
    res = get_res('data', 'add_admin', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('添加团队成员接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_add_admin(self):
        u"""添加团队成员接口"""
        create_team()
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
        delete_team(teamId)
        logger.info('删除团队成功')
