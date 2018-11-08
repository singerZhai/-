import requests
import pytest
import allure
from base.base_action import get_url, get_params, get_token, get_res


class TestChangePassword:

    change_url = get_url('data', 'change_password', 'url')
    change_params = get_params('data', 'change_password', 'params')
    userToken = get_token()
    new_params = dict(change_params, **userToken)
    change_res = get_res('data', 'change_password', 'res')

    # 修改密码接口
    @pytest.mark.skipif(condition=True, reason='更改密码涉及更改yml数据，选择跳过')
    @allure.step('修改密码接口')
    def test_change_password(self):
        r = requests.post(self.change_url, self.new_params)
        res = r.json()
        assert res['status'] == self.change_res['status']
        assert res['msg'] == self.change_res['msg']