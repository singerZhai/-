import unittest
import requests
import json
from base.base_action import get_url, get_res, now_time, start_log, runtime, end_log, params_log, res_log, \
    assert_equal, get_token, get_params, get_id, create_team, delete_team, get_team_id
from base.logger import Log


class TestEditTeamMember(unittest.TestCase):

    url = get_url('data', 'edit_team_member', 'url')
    params = get_params('data', 'edit_team_member', 'params')
    res = get_res('data', 'edit_team_member', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('编辑团队成员接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_edit_team_member(self):
        u"""编辑团队成员接口"""
        create_team()
        logger.info('创建团队')
        teamId = get_team_id()
        logger.info('获取teamId')
        id = get_id()
        logger.info('获取teamId')
        userToken = get_token()
        logger.info('获取token')
        new_params = dict(userToken, **id, **self.params)
        logger.warning(params_log + str(new_params))
        r = requests.post(url=self.url, data=new_params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
        delete_team(teamId)
