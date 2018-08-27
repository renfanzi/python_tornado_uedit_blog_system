#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os
import re
import json
import tornado.web
from app import static_path
from controllers.HomeHandlers import *
from common.Base import *
from common.tools.uploader import Uploader
from core.ShowDetails import *
from common.error import *
from common.tools.page_item import Pagination


class ShowAdminHtmlHandler(SessionBaseHandler):
    def get(self, *args, **kwargs):
        if self.session["is_login"]:
            self.render('admin/admin.html')
        else:
            self.redirect("/login.html")


# -----<查看我的文章目录_render_html>----- #

class ShowArticleDirectoriesHtmlHandler(SessionBaseHandler):
    def get(self):
        if self.session["is_login"]:
            self.render('admin/article_directories.html')
        else:
            self.redirect("/login.html")


# -----<查看用户的文章分类>----- #

class ShowCategoryHandler(SessionBaseHandler):
    def post(self, *args, **kwargs):
        self.asynchronous_post()

    def _post(self):
        try:
            status = 2000
            userID = self.get_argument('UserID', '123456')
            if not userID:
                raise ValueError
            data = ShowCategoryDetail(userID)
        except Exception as e:
            status = 4002
            data = []
            my_log.error(e)
        return result(status=status, value=data)


# -----<查看单个用户所有文章>----- #

class ShowSampleUserAllArticleHandler(SessionBaseHandler):
    def post(self, *args, **kwargs):
        self.asynchronous_post()

    def _post(self):

        if self.session["is_login"]:
            status = 2000
            UserID = self.get_argument("UserID", None)
            data = []
            try:
                if UserID:
                    data = ShowAllArticleDetail(UserID)
                else:
                    raise CustomException(4002)
            except CustomException as e:
                status = int(e.message[1:5])
                my_log.error(e)
            except Exception as e:
                my_log.error(e)
                status = 5000
            return result(status=status, value=data)
        else:
            return self.noLogin()

    def noLogin(self):
        return result(status=4005)

class ShowSingleArticleHandler(SessionBaseHandler):
    def post(self, *args, **kwargs):
        self.asynchronous_post()

    def _post(self):

        if self.session["is_login"]:
            status = 2000
            UserID = self.get_argument("UserID", None)
            TextID = self.get_argument("ID", None)
            data = {}
            try:
                data = ShowSingleArticleDetail(UserID, TextID)
            except CustomException as e:
                status = int(e.message[1:5])
                my_log.error(e)
            except Exception as e:
                my_log.error(e)
                status = 5000
            return result(status=status, value=data)
        else:
            status = 2000
            UserID = self.get_argument("UserID", None)
            TextID = self.get_argument("ID", None)
            data = {}
            try:
                data = ShowSingleArticleDetail(UserID, TextID)
            except CustomException as e:
                status = int(e.message[1:5])
                my_log.error(e)
            except Exception as e:
                my_log.error(e)
                status = 5000
            return result(status=status, value=data)

    def noLogin(self):
        return result(status=4005)



# -----<查看网站首页html>----- #

class ShowHomeIndexHandler(BaseHandler):
    def post(self, *args, **kwargs):
        self.render('performs/index_home.html')

    def get(self, *args, **kwargs):
        self.render('performs/index_home.html')


class ShowNumberedMusicalNotationHandler(BaseHandler):
    def post(self, *args, **kwargs):
        self.render('performs/numbered_musical_notation.html')

    def get(self, *args, **kwargs):
        self.render('performs/numbered_musical_notation.html')


class ShowHomeJianpuHandler(BaseHandler):
    def post(self, *args, **kwargs):
        self.render('performs/jianpu.html')

    def get(self, *args, **kwargs):
        self.render('performs/jianpu.html')



class ShowOtherHtmlHandler(BaseHandler):
    def post(self, *args, **kwargs):
        self.redirect('/index_home.html')

    def get(self, *args, **kwargs):
        self.redirect('/index_home.html')


# -----<查看分页>----- #

class ShowPagerHandler(BaseHandler):
    def post(self, *args, **kwargs):
        self.asynchronous_post()

    def _post(self):
        data = [1, 2]
        try:
            status = 2000
            userID = self.get_argument('UserID', '123456')
            Flag = self.get_argument('Flag', 'numbered_musical_notation')
            if not userID:
                raise ValueError
            if Flag == "numbered_musical_notation":
                data = ShowPagerDetail(userID)

        except Exception as e:
            status, msg = FormatErrorCode(e)
            my_log.error("({},{})".format(status, msg))

        return result(status=status, value=data)


# -----<查看分页数据>----- #

class ShowPagerDataHandler(BaseHandler):
    def post(self, *args, **kwargs):
        self.asynchronous_post()

    def _post(self):
        data = []
        try:
            status = 2000
            userID = self.get_argument('UserID', '123456')
            Flag = self.get_argument('Flag', 'numbered_musical_notation')
            Pager = int(self.get_argument('Pager', 1))
            if not userID:
                raise ValueError
            if Flag == "numbered_musical_notation":
                data = ShowPagerDataDetail(userID, Pager)


        except Exception as e:
            status, msg = FormatErrorCode(e)
            my_log.error("({},{})".format(status, msg))

        return result(status=status, value=data)
