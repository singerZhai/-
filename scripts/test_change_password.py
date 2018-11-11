from time import sleep
import requests
import pytest
import allure
from base.base_action import get_url, get_params, get_token, get_res, change_back_password_params, \
    again_change_password, assert_equal


class TestChangePassword:

    change_url = get_url('data', 'change_password', 'url')
    change_params = get_params('data', 'change_password', 'params')
    change_res = get_res('data', 'change_password', 'res')
    change_back_password_params = change_back_password_params()

    # 修改密码接口
    @allure.step('修改密码接口')
    @pytest.mark.skipif(condition=False, reason='第二次修改密码token异常')
    def test_change_password(self):
        userToken = get_token()
        # 拼接两个字典
        new_params = dict(self.change_params, **userToken)
        r = requests.post(self.change_url, new_params)
        res = r.json()
        assert r.status_code == 200
        assert res['status'] == self.change_res['status']
        assert res['msg'] == self.change_res['msg']
        # sleep作用：解决频繁调用接口报错问题
        sleep(3)
        # 将更改后密码再次更改回123456，使case能够正常执行
        again_change_password()
        # sleep作用：解决频繁调用接口报错问题
        sleep(3)
