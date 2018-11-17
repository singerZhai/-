import unittest
import requests
from base.base_action import get_url, get_res, get_params


class TestSelectMeetingModifyRecords(unittest.TestCase):

    url = get_url('data', 'select_meeting_modify_records', 'url')
    params = get_params('data', 'select_meeting_modify_records', 'params')
    res = get_res('data', 'select_meeting_modify_records', 'res')

    def test_select_meeting_modify_records(self):
        u"""会议变更记录查询接口"""
        # 将meetingId写死了(9280)，是一个之前做过编辑操作的预约会议
        r = requests.post(self.url, self.params)
        res = r.json()
        print(res)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(res['status'], self.res['status'])
        self.assertEqual(res['msg'], self.res['msg'])
