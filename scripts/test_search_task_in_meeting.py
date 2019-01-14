import json
import unittest
import requests
from base.base_action import get_url, get_res, get_token, create_task_in_meeting_and_return_meeting_id, \
    select_task_list_and_meetingId_by_create_task, get_first_task_id_by_task_list, delete_by_taskId, end_meeting, \
    start_log, params_log, res_log, end_log, now_time, runtime, assert_equal
from base.logger import Log


class TestSearchTaskInMeeting(unittest.TestCase):

    url = get_url('data', 'search_task_in_meeting', 'url')
    res = get_res('data', 'search_task_in_meeting', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('查询会议中的任务接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_search_task_in_meeting(self):
        u"""查询会议中的任务接口"""
        meetingId_dict = create_task_in_meeting_and_return_meeting_id()
        logger.info('获取meetingId')
        userToken = get_token()
        logger.info('获取token')
        params = dict(userToken, **meetingId_dict)
        logger.warning(params_log + str(params))
        r = requests.post(self.url, params)
        res = r.json()
        result = json.dumps(res, ensure_ascii=False)
        logger.warning(res_log + result)
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
        task_list, meetingId = select_task_list_and_meetingId_by_create_task()
        logger.info('获取任务列表和meetingId')
        taskId = get_first_task_id_by_task_list(task_list)
        logger.info('获取taskId')
        delete_by_taskId(taskId)
        logger.info('结束任务')
        end_meeting(meetingId)
        logger.info('结束会议')
