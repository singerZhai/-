import requests

from base.base_action import get_url, get_params, get_res


class TestSignInDeviceUser:

    url = get_url('data', 'sign_in_device_user', 'url')
    params = get_params('data', 'sign_in_device_user', 'params')
    res = get_res('data', )