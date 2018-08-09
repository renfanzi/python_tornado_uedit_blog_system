#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
from controllers.HomeHandlers import *
from common.Base import result, MyGuid, my_datetime, Config, my_log

'''

以后这个handlers主要写关于登录注册找回密码等


'''

"""
    登录页面
"""


class LoginHtmlHandler(BaseController):
    def get(self, *args, **kwargs):
        self.render('admin/login.html')


"""
    登录接口
"""


class SignInHandler(SessionBaseHandler):
    def post(self, *args, **kwargs):
        self.asynchronous_post()

    def _post(self):
        user = Config().get_content("user")
        user_name = self.get_argument("UserName", None)
        pass_word = self.get_argument("PassWord", None)
        if user_name and pass_word:
            if str(user["user_name"]) == str(user_name) and str(user["pass_word"]) == str(pass_word):
                self.session["is_login"] = True
                return result(status=2000)
            else:
                return result(status=4005)
        else:
            return result(status=4005)
