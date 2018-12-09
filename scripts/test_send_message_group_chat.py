import unittest
import requests
from base.base_action import get_url, get_params, get_res, get_group_id_by_task_list, \
    select_task_list_and_meetingId_by_create_task, get_first_task_id_by_task_list, end_meeting, delete_by_taskId, \
    start_log, params_log, end_log, res_log, now_time, runtime, assert_equal
from base.logger import Log


class TestSendMessageGroupChat(unittest.TestCase):
    url = get_url('data', 'send_message_group_chat', 'url')
    params = get_params('data', 'send_message_group_chat', 'params')
    res = get_res('data', 'send_message_group_chat', 'res')

    def setUp(self):
        global logger
        logger = Log()
        global start_time
        start_time = now_time()
        logger.warning(start_log)
        logger.info('群聊消息发送接口')

    def tearDown(self):
        run_time = runtime(start_time)
        logger.warning(run_time)
        logger.warning(end_log)

    def test_send_message_group_chat(self):
        u"""群聊消息发送接口"""
        task_list_msg, meetingId = select_task_list_and_meetingId_by_create_task()
        logger.info('通过创建会议和任务来获取任务列表和meetingId')
        groupId = get_group_id_by_task_list(task_list_msg)
        logger.info('获取groupId')
        new_params = dict(groupId, **self.params)
        logger.info(params_log + str(new_params))
        files = {'contentPic': open('./data/photo.jpg', 'rb')}
        logger.info('上传文件为: ./data/photo.jpg')
        r = requests.post(self.url, params=new_params, files=files)
        res = r.json()
        logger.info(res_log + str(res))
        assert_equal(r.status_code, 200)
        assert_equal(res['status'], self.res['status'])
        assert_equal(res['msg'], self.res['msg'])
        task_id = get_first_task_id_by_task_list(task_list_msg)
        logger.info('获取taskId')
        end_meeting(meetingId)
        logger.info('结束会议')
        delete_by_taskId(task_id)
        logger.info('结束任务')
