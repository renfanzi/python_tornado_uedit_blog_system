#!/usr/bin/env python
# -*- coding:utf-8 -*-

from controllers.HomeHandlers import SessionBaseHandler
from common.Base import *
from models.UpdateModels import *




class UpdateEditArticleHtmlHandler(SessionBaseHandler):
    def get(self):
        if self.session["is_login"]:
            self.render('admin/edit_article.html')
        else:
            self.redirect("/login.html")



class DelectArticleHandler(SessionBaseHandler):
    def post(self, *args, **kwargs):
        self.asynchronous_post()

    def _post(self):

        if self.session["is_login"]:
            status = 2000
            UserID = Config().get_content("user")["UserID"]
            article_id = self.get_argument("article_id", None)
            data = []
            try:
                if UserID and article_id:
                    DeleteArticleModel(UserID, article_id)
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
