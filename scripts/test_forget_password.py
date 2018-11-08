import allure
import requests
import pytest
from base.base_action import get_url, get_params, get_res


class TestForgetPassword:

    forget_url = get_url('data', 'forget_password', 'url')
    forget_params = get_params('data', 'forget_password', 'params')
    forget_res = get_res('data', 'forget_password', 'res')

    @pytest.mark.skipif(condition=True, reason='万能验证码')
    @allure.step('用户忘记密码接口')
    def test_forget_password(self):
        r = requests.post(self.forget_url, self.forget_params)
        res = r.json()
        assert res['status'] == self.forget_res['status']
        assert res['msg'] == self.forget_res['msg']
