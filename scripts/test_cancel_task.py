import unittest
import requests
from base.base_action import get_url, get_res, select_task_list_and_meetingId_by_create_task, get_token, end_meeting, \
    get_first_task_id_by_task_list, delete_by_taskId, res_log, params_log, start_log, end_log, now_time, runtime, \
    end_meeting_log, end_task_log, assert_equal
from base.logger import Log


class TestCancelTask(unittest.TestCase):

    url = get_url('data', 'cancel_task', 'url')
    res = get_res('data', 'cancel_task', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('取消任务接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_cancel_task(self):
        u"""取消任务接口"""
        task_list, meetingId = select_task_list_and_meetingId_by_create_task()
        logger.info('创建任务并获取任务列表和meetingId')
        taskId = get_first_task_id_by_task_list(task_list)
        logger.info('利用任务列表提取taskId')
        userToken = get_token()
        logger.info('获取token')
        params = dict(taskId, **userToken)
        logger.info(params_log + str(params))
        r = requests.post(self.url, params)
        res = r.json()
        logger.info(res_log + str(res))
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
        end_meeting(meetingId)
        logger.info(end_meeting_log)
        delete_by_taskId(taskId)
        logger.info(end_task_log)
