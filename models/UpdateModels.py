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


def UpdateArticleModel(info):
    str_li = ["ArticleTitle", "AllHtml", "WriteHtmlContent", "WriteHtml", "Password", "Tag", "Friends", "CategoryID",
              "HomeImage"]
    sub_str_li = ["AllHtml", "WriteHtmlContent", "WriteHtml"]
    cadition_value = ''

    value = []
    for i in info:
        if i in str_li:
            cadition_value += '`' + i + '` = "%s" , '
            if i in sub_str_li:
                value.append(info[i])
            else:
                value.append(info[i])
        elif i == "ID":
            continue
        else:
            cadition_value += '`' + i + '` = %s , '
            value.append(info[i])
    cadition_value = cadition_value.rstrip(", ")

    sql = \
        """
            Update `blog`.`text`
            SET
                {} where {};
        """.format(cadition_value, " `ID` = {}".format(info["ID"]))

    ret = MyPymysql('notdbMysql')
    ret.idu_sql(sql, value=tuple(value))
    ret.close()
