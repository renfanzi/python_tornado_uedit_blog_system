#!/usr/bin/env python
# -*- coding:utf-8 -*-

from models.ShowModels import *
from common.tools.page_item import Pagination

def ShowCategoryDetail(userID):
    return ShowCategoryModel(userID)


def ShowAllArticleDetail(UserID):
    return ShowAllArticleModel(UserID)


def ShowSingleArticleDetail(UserID, TextID):
    return ShowSingleArticleModel(UserID=UserID, TextID=TextID)


def ShowPagerDetail(UserID):
    page_obj = ShowPagerInfoModel()
    data = page_obj.ShowPager(UserID)
    page_obj.close()

    obj = Pagination(data["count"])
    data_count = obj.item_pages
    return data_count

def ShowPagerDataDetail(UserID, Pager):
    page_obj = ShowPagerInfoModel()
    page = page_obj.ShowPager(UserID)


    obj = Pagination(page["count"], Pager)
    data_count = obj.item_pages

    page_data = page_obj.ShowPagerData(UserID, obj.start)
    page_obj.close()
    return page_data