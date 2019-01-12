import json
import unittest
import requests
from base.base_action import get_url, get_res, select_task_list_and_meetingId_by_create_task, \
    get_first_task_id_by_task_list, get_token, end_meeting, delete_by_taskId, start_log, params_log, \
    res_log, end_log, now_time, runtime, assert_equal
from base.logger import Log


class TestDeleteByTaskId(unittest.TestCase):

    url = get_url('data', 'delete_by_taskId', 'url')
    res = get_res('data', 'delete_by_taskId', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('删除指定的任务记录接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_delete_by_taskId(self):
        u"""删除指定的任务记录接口"""
        task_list, meetingId = select_task_list_and_meetingId_by_create_task()
        logger.info('创建快速会议并获取任务列表信息')
        taskId = get_first_task_id_by_task_list(task_list)
        logger.info('通过任务列表获取taskId')
        userToken = get_token()
        logger.info('获取token')
        params = dict(userToken, **taskId)
        logger.info(params_log + str(params))
        r = requests.post(self.url, params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
        end_meeting(meetingId)
        logger.info('结束会议')
        delete_by_taskId(taskId)
        logger.info('结束任务')
