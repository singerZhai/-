import json
import unittest
import requests
from base.base_action import get_url, get_params, get_res, get_task_begin_time, get_task_end_time, \
    get_token, end_meeting, get_meeting_id_with_create_fast_meeting, params_log, res_log, start_log, \
    end_log, now_time, runtime, assert_equal
from base.logger import Log


class TestCreateTask(unittest.TestCase):

    url = get_url('data', 'create_task', 'url')
    params = get_params('data', 'create_task', 'params')
    res = get_res('data', 'create_task', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('创建新的任务接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_create_task(self):
        u"""创建新的任务接口"""
        meetingId = get_meeting_id_with_create_fast_meeting()
        logger.info('创建快速会议并获取meetingId：' + str(meetingId))
        beginTime = get_task_begin_time()
        endTime = get_task_end_time()
        userToken = get_token()
        logger.info('获取token')
        new_params = dict(userToken, **meetingId, **beginTime, **endTime, **self.params)
        logger.warning(params_log + str(new_params))
        r = requests.post(self.url, new_params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
        end_meeting(meetingId)
        logger.info('关闭会议')
