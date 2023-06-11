import requests
import datetime
from loguru import logger


class base:
    host_name = "https://api.dingtalk.com/v1.0"
    token = None

    def __init__(self, token: str=None):
        """init

        Args:
            token (str, optional): . Defaults to None.
        """
        if token:
            self.token = token

    def request(self, api_name, method="GET", **kwargs):
        url = f"{self.host_name}/{api_name}"

        # headers = kwargs.get("headers", {})
        # headers["content-type"] = "application/x-www-form-urlencoded"
        # headers["accept-type"] = "application/json, text/javascript, */*; q=0.01"
        # kwargs["headers"] = headers

        params = kwargs.get("params", {})
        if self.token:
            params["access_token"] = self.token
        kwargs["params"] = params

        logger.debug(dict(msg="正在请求的url:", url=url))
        logger.debug(dict(msg="正在请求的参数:", kwargs=kwargs))

        response = requests.request(method=method, url=url, **kwargs,)
        if response.status_code == 200:
            return self.response(response.json())
        logger.error(
            {"msg": "请求错误", "data": response.json(),}
        )

    def response(self, data):
        logger.debug(dict(msg="返回值", response=data))
        return data