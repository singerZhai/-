import unittest
import requests
from base.base_action import get_url, get_params, get_res, get_task_begin_time, get_task_end_time, get_token, \
    end_meeting, select_task_list_and_meetingId_by_create_task, \
    get_first_task_id_by_task_list, delete_by_taskId, start_log, params_log, res_log, end_log, now_time, runtime, \
    assert_equal
from base.logger import Log


class TestEditAppointTaskMsg(unittest.TestCase):

    url = get_url('data', 'edit_appoint_task_msg', 'url')
    params = get_params('data', 'edit_appoint_task_msg', 'params')
    res = get_res('data', 'edit_appoint_task_msg', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('编辑指定任务的详细信息接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_edit_appoint_task_msg(self):
        u"""编辑指定任务的详细信息接口"""
        task_list, meetingId = select_task_list_and_meetingId_by_create_task()
        logger.info('会议中创建任务并获取任务列表和meetingId')
        taskId = get_first_task_id_by_task_list(task_list)
        logger.info('通过任务列表获取taskId')
        edit_begin_time = get_task_begin_time()
        edit_end_time = get_task_end_time()
        userToken = get_token()
        logger.info('获取token')
        new_params = dict(userToken, **taskId, **meetingId, **edit_begin_time, **edit_end_time, **self.params)
        logger.info(params_log + str(new_params))
        r = requests.post(self.url, new_params)
        res = r.json()
        logger.info(res_log + str(res))
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
        delete_by_taskId(taskId)
        logger.info('结束任务')
        end_meeting(meetingId)
        logger.info('结束会议')
