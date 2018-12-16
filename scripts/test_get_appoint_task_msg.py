import json
import unittest
import requests

from base.base_action import get_url, get_res, select_task_list_and_meetingId_by_create_task, \
    get_first_task_id_by_task_list, delete_by_taskId, end_meeting, start_log, res_log, end_log, now_time, runtime, \
    assert_equal
from base.logger import Log


class TestGetAppointTaskMsg(unittest.TestCase):

    url = get_url('data', 'get_appoint_task_msg', 'url')
    res = get_res('data', 'get_appoint_task_msg', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('获取指定任务的详细信息接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_get_appoint_task_msg(self):
        u"""获取指定任务的详细信息接口"""
        task_list, meetingId = select_task_list_and_meetingId_by_create_task()
        logger.info('在会议中创建任务并获取任务列表和meetingId')
        taskId = get_first_task_id_by_task_list(task_list)
        logger.info('获取taskId')
        r = requests.post(self.url, taskId)
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
