#!/usr/bin/env python
# -*- coding:utf-8 -*-

from models.CreateModel import *
from common.Base import *
from common.tools.uploader import UploadFile
from common.tools.pil_image import ThumbNailImg
from app import static_path

def AddArticleClassDetail(title, description, UserID):
    return AddArticleClassModel(title, description, UserID)

def AddArticleDetail(info, article_little_img, static_path):

    uploader = UploadFile(article_little_img, static_path)
    fileInfo = uploader.getFileInfo()

    thumbNailFilePathName = ThumbNailImg(fileInfo["filePathName"])
    subthumbNailFilePathName = thumbNailFilePathName.replace(static_path, "")
    UserID = Config().get_content("user")["user_id"]
    info["UserID"] = UserID
    info["CreateTime"] = my_datetime.str_datetime()
    info["HomeImage"] = subthumbNailFilePathName

    return AddArticleModel(info)