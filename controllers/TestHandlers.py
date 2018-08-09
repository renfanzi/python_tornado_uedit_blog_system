#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
import json
import tornado.web
from app import static_path
from controllers.HomeHandlers import BaseController, BaseHandler, SessionBaseHandler
from common.Base import *
from common.tools.uploader import Uploader
from core.ShowDetails import *



class TestUploadFileHtmlHandler(BaseController):
    def get(self, *args, **kwargs):
        self.render('test.html')


class TestUploadFileHandler(BaseHandler):
    def post(self, *args, **kwargs):
        self.asynchronous_post()

    def _post(self):
        file1 = self.request.files["file1"]
        file2 = self.request.files["file2"]

        print(file1[0]["filename"])
        print(file2[0]["filename"])
        return '0'



class TestSignInHandler(SessionBaseHandler):
    def get(self, *args, **kwargs):
        self.asynchronous_get()

    def _get(self):
        self.session["is_login"] = True

        # for i in range(20):
        #     print(i)
        #     print(time.sleep(1))
        #
        print(self.session["is_login"])


        return result(2000)

class TestSignIn2Handler(SessionBaseHandler):
    def get(self, *args, **kwargs):
        self.asynchronous_get()

    def _get(self):
        print("22222", self.session["is_login"])
        print(self.get_cookie("__sessionId__"))

        return result(2000)