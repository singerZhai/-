import json
import unittest
import requests
from base.base_action import get_url, get_params, get_res, select_task_list_and_meetingId_by_create_task, \
    get_first_task_id_by_task_list, get_token, end_meeting, delete_by_taskId, start_log, params_log, res_log, end_log, \
    now_time, runtime, assert_equal
from base.logger import Log


class TestModifyTaskSchedule(unittest.TestCase):

    url = get_url('data', 'modify_task_schedule', 'url')
    params = get_params('data', 'modify_task_schedule', 'params')
    res = get_res('data', 'modify_task_schedule', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('修改任务进度接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_modify_task_schedule(self):
        u"""修改任务进度接口"""
        task_list, meetingId = select_task_list_and_meetingId_by_create_task()
        logger.info('获取任务列表和meetingId')
        taskId = get_first_task_id_by_task_list(task_list)
        logger.info('获取taskId')
        userToken = get_token()
        logger.info('获取token')
        new_params = dict(userToken, **taskId, **self.params)
        logger.info(params_log + str(new_params))
        r = requests.post(self.url, new_params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.info(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
        delete_by_taskId(taskId)
        logger.info('结束任务')
        end_meeting(meetingId)
        logger.info('结束会议')
