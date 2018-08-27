#!/usr/bin/env python
# -*- coding:utf-8 -*-

from controllers.HomeHandlers import SessionBaseHandler
from common.Base import *
from models.UpdateModels import *
import json
from controllers.HomeHandlers import *
from core.AddDetails import *
from common.Base import *
from app import static_path
from common.tools.uploader import UploadFile
from core.UpdateDetails import *




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


# -----<更新文章>------ #
class UpdateArticleHandler(SessionBaseHandler):
    def post(self, *args, **kwargs):
        self.asynchronous_post()

    def _post(self):

        if self.session["is_login"]:
            status = 2000
            info = self.get_argument("info", None)
            info = json.loads(info) if info else None

            try:
                if info :
                    if self.request.files and self.request.files["article_little_img"][0]['filename'].split('.')[1].lower() in ["png", "jpg", "jpeg", "gif"]:
                        article_little_img = self.request.files["article_little_img"][0]
                        UpdateArticleDetail(info, article_little_img, static_path)
                    else:
                        UpdateArticleDetail(info, None, static_path)
                else:
                    pass
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