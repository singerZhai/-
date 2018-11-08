import allure
import requests
import pytest

from base.base_action import get_url, get_res, get_token


class TestSearchUserMsg:

    search_user_msg_url = get_url('data', 'search_user_msg', 'url')
    search_user_msg_res = get_res('data', 'search_user_msg', 'res')

    @allure.step('查询用户接口')
    def test_search_user_msg(self):
        user_token = get_token()
        r = requests.post(self.search_user_msg_url, user_token)
        res = r.json()
        assert res['status'] == self.search_user_msg_res['status']
        assert res['msg'] == self.search_user_msg_res['msg']
