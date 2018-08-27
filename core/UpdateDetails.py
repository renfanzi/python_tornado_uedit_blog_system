#!/usr/bin/env python
# -*- coding:utf-8 -*-

from models.CreateModel import *
from common.Base import *
from common.tools.uploader import UploadFile
from common.tools.pil_image import ThumbNailImg
from models.UpdateModels import *
from app import static_path

def UpdateArticleDetail(info, article_little_img, static_path):
    '''
    需求： 什么变了更新什么
    :param info:
    :param article_little_img:
    :param static_path:
    :return:
    '''
    if article_little_img:
        uploader = UploadFile(article_little_img, static_path)
        fileInfo = uploader.getFileInfo()

        thumbNailFilePathName = ThumbNailImg(fileInfo["filePathName"])
        subthumbNailFilePathName = thumbNailFilePathName.replace(static_path, "")
        UserID = Config().get_content("user")["user_id"]
        info["HomeImage"] = subthumbNailFilePathName

    return UpdateArticleModel(info)