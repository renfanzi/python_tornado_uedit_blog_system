#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
from controllers.HomeHandlers import *
from core.AddDetails import *
from common.Base import *
from app import static_path
from common.tools.uploader import UploadFile


class MyTestHandler(BaseHandler):
    def get(self):
        self.asynchronous_get()

    def _get(self):
        user = self.get_argument('user', None)
        print("get", user)
        ret = json.dumps(result(status=2000, value="hello world!"), ensure_ascii=False)
        return ret

    def post(self, *args, **kwargs):
        self.asynchronous_post()

    def _post(self):
        user = self.get_argument('user', None)
        print("post", user)
        ret = result(status=2000, value="hello world!")
        return ret


class CreateProjectHandler(initializeBaseRequestHandler):
    def post(self, *args, **kwargs):
        self.asynchronous_post()

    def _post(self):
        if self.verifyFlag == 1 and self.status == 0:
            return result(status=2000, value="hello world!")
        else:
            return self.noLogin()

    def noLogin(self):
        return result(status=4005)


"""
    创建文章 render html handler
"""


class AddArticleHtmlHandler(SessionBaseHandler):
    def get(self, *args, **kwargs):
        if self.session["is_login"]:
            self.render('admin/create_article.html')
        else:
            self.redirect('/login.html')


'''
    添加文章：
        数据到数据库
'''


class AddArticleHandler(SessionBaseHandler):
    def post(self, *args, **kwargs):
        self.asynchronous_post()

    def _post(self):


        if self.session["is_login"]:
            status = 2000
            info = self.get_argument("info", None)
            info = json.loads(info) if info else None
            article_little_img = self.request.files["article_little_img"][0]

            try:
                if info :
                    if article_little_img['filename'].split('.')[1].lower() in ["png", "jpg", "jpeg", "gif"]:
                        AddArticleDetail(info, article_little_img, static_path)
                    else:
                        raise CustomException(4000)
                else:
                    raise CustomException(4002)
            except CustomException as e:
                status = int(e.message[1:5])
                my_log.error(e)
            except Exception as e:
                my_log.error(e)
                status = 5000
            return result(status=status)
        else:
            return self.noLogin()

    def noLogin(self):
        return result(status=4005)


class EditClassifyHtmlHandler(SessionBaseHandler):
    def get(self):
        if self.session["is_login"]:
            self.render("admin/edit_classify.html")
        else:
            self.redirect("/login.html")


"""
    文章分类页面：
        添加文章分类
"""


class AddArticleClassHandler(SessionBaseHandler):
    def post(self, *args, **kwargs):
        self.asynchronous_post()

    def _post(self):
        if self.session["is_login"]:
            title = self.get_argument("title", None)
            description = self.get_argument("description", None)
            status = 2000

            try:
                if title and description:
                    AddArticleClassDetail(title, description, self.UserID)
                else:
                    raise CustomException(4002)
            except CustomException as e:
                status = int(e.message[1:5])
                my_log.error(e)
            except Exception as e:
                my_log.error(e)
                status = 5000

            return result(status=status)
        else:
            return self.noLogin()

    def noLogin(self):
        return result(status=4005)
