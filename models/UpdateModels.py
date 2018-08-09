#!/usr/bin/env python
# -*- coding:utf-8 -*-


from common.Base import *


def DeleteArticleModel(UserID, ID):
    sql = """
        UPDATE
        SET blog.text ArticleStatus = 0
        WHERE
            UserID ={}
        AND ID ={};
        """.format(UserID, ID)
    ret = MyPymysql('notdbMysql')
    ret.idu_sql(sql)
    ret.close()