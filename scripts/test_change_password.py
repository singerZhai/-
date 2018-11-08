import requests
import pytest
import allure

from base.base_action import get_url, get_params, get_token, get_res


class TestChangePassword:

    change_url = get_url('data', 'change_password', 'url')
    change_params = get_params('data', 'change_password', 'params') + get_token()
    change_res = get_res('data', 'change_password', 'res')

    # 修改密码接口
    @allure.step('修改密码接口')
    def test_change_password(self):
        r = requests.post(self.change_url, self.change_params)
        res = r.json()
        assert res['status'] == self.change_res['status']
        assert res['msg'] == self.change_res['msg']